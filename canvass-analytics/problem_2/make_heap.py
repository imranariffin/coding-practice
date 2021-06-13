import heapq
from multiprocessing import Pool
import typing as t

from .utils import (
    COLUMN_FACTORIES,
    COLUMN_DEFAULTS,
    ColumnNames,
    Row,
    make_chunk_file_name,
)


def make_n_heaps(
    num_of_heaps: int,
    ifile_name: str,
    sort_columns: t.Tuple[ColumnNames, ...],
) -> None:
    with Pool(processes=num_of_heaps) as pool:
        for chunk_id in range(num_of_heaps):
            pool.apply_async(make_heap, (chunk_id, num_of_heaps, ifile_name, sort_columns))
        pool.close()
        pool.join()


def make_heap(
    chunk_id: int,
    num_of_chunks: int,
    ifile_name: str,
    sort_columns: t.Tuple[ColumnNames, ...]
) -> None:
    """
    Given an input filename, store a specific portion of content as heap-sorted.

    By "specific portion" we mean every `chunk_id`th line of the input file. This function should be
    idempotent.
    """
    priority_queue = []

    with open(ifile_name) as csvfile:
        for i, line in enumerate(csvfile):
            if i == 0:
                continue
            if num_of_chunks > 1 and i % num_of_chunks != chunk_id:
                continue

            _row = Row(*line.rstrip("\n").split(","))
            row = Row(
                *(
                    COLUMN_FACTORIES[column_name](getattr(_row, column_name)) or COLUMN_DEFAULTS[column_name]
                    for column_name in _row._fields
                )
            )
            sort_key = tuple(
                getattr(row, column_name.value)
                for column_name in sort_columns
            )
            priority_queue.append((sort_key, row))

    heapq.heapify(priority_queue)

    header = ",".join(column_name.value for column_name in ColumnNames)
    raw_output_lines: t.List[str] = [header]
    while priority_queue:
        _, heap_row = heapq.heappop(priority_queue)
        output_line = ",".join(str(value) for value in heap_row)
        raw_output_lines.append(output_line)
    raw_output_line = "\n".join(raw_output_lines)

    ofile_name = make_chunk_file_name(base_file_name=ifile_name, chunk_id=chunk_id)
    with open(ofile_name, "w") as ofile:
        ofile.writelines(raw_output_line)
        print(f"DONE Sorting for chunk {chunk_id}")


def _test():
    num_of_chunks = 20
    make_n_heaps(
        num_of_heaps=num_of_chunks,
        ifile_name="./random_data.csv",
        # ifile_name="./large_data.csv",
        sort_columns=(ColumnNames.DEVICE_ID, ColumnNames.DATE),
    )
