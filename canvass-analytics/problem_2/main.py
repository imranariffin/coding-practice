from .make_heap import make_heap
from .utils import NUM_OF_CHUNKS, ColumnNames


def main():
    # ifile_name = "./large_data.csv"
    ifile_name = "./random_data.csv"
    make_heap(
        chunk_id=1,
        num_of_chunks=NUM_OF_CHUNKS,
        ifile_name=ifile_name,
        sort_columns=(ColumnNames.DEVICE_ID, ColumnNames.DATE),
    )


if __name__ == "__main__":
    main()