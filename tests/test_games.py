import csv
import os

DATA_DIR = "data"

csv_files = [
    "clicks.csv",
    "conversions.csv",
    "impressions.csv"
]


def test_data_folder_exists():
    assert os.path.exists(DATA_DIR)


def test_csv_files_exists():
    for file_name in csv_files:
        file_path = os.path.join(DATA_DIR,file_name)
        assert os.path.exists(file_path)


def test_csv_files_are_not_empty():

    for file_name in csv_files:
        file_path = os.path.join(DATA_DIR,file_name)

        with open(file_path , newline="") as file:
            rows = list(csv.reader(file))

        assert len(rows) > 1


def test_required_column():
    required_columns = {
        "clicks.csv": ["click_id","impression_id","campaign_id","event_timestamp","received_timestamp","device_id"],
        "conversions.csv" : ["conversion_id","device_id","game_id","revenue_usd","event_timestamp","received_timestamp","conversion_type"],
        "impressions.csv" : ['impression_id','campaign_id','game_id','cost_usd','event_timestamp','received_timestamp','platform']
    }


    for file_name, columns in required_columns.items():

        with open(f"data/{file_name}", newline="") as file:
            header = next(csv.reader(file))

        for column in columns:
            assert column in header



# def test_no_empty_values():
#     for file_name in csv_files:
#         with open(f"data/{file_name}", newline="") as file:
#             reader = csv.DictReader(file)

#             for row_number, row in enumerate(reader, start=2):
#                 for column, value in row.items():
#                     assert value is not None, (
#                         f"{file_name}: row {row_number}, "
#                         f"column '{column}' is NULL"
#                     )

#                     assert value.strip() != "", (
#                         f"{file_name}: row {row_number}, "
#                         f"column '{column}' is empty"
#                     )



# def test_duplicate_ids():
#     for file_name, id_column in {
#         "clicks.csv": "click_id",
#         "conversions.csv": "conversion_id",
#         "impressions.csv": "impression_id"
#     }.items():

#         with open(f"data/{file_name}", newline="") as file:
#             reader = csv.DictReader(file)
#             ids = [row[id_column] for row in reader]

#         duplicates = {
#             id_value
#             for id_value in ids
#             if ids.count(id_value) > 1
#         }

#         if duplicates:
#             print(f"\nFile: {file_name}")
#             print(f"Duplicate {id_column}: {duplicates}")
#             print(f"Number of duplicate IDs: {len(duplicates)}")

#         assert not duplicates