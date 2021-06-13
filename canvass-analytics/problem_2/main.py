from .make_chunks import make_n_chunks
from .merge_chunks import merge_chunks
from .utils import NUM_OF_CHUNKS, ColumnNames


def main():
    # ifile_name = "./large_data.csv"
    ifile_name = "./random_data.csv"
    sort_columns = (ColumnNames.DEVICE_ID, ColumnNames.DATE)
    make_n_chunks(
        num_of_heaps=NUM_OF_CHUNKS,
        ifile_name=ifile_name,
        sort_columns=sort_columns,
    )
    merge_chunks(
        base_ifile_name=ifile_name,
        chunk_ids=list(range(NUM_OF_CHUNKS)),
        ofile_name="./output.csv",
        sort_columns=sort_columns,
    )


if __name__ == "__main__":
    main()