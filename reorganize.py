import os
import pandas as pd
import glob

abs_dir_path = os.path.dirname(os.path.realpath(__file__))  # abosolute path of the current .py file
father_dir = abs_dir_path  + "\\data\\Light intensity-5.5 test\\delete_center_column"
ex_id = "60"
target_dir = os.path.join(father_dir, ex_id)
cells = [1,2,3,4,5,6]
for cell in cells:
    out_summary_file = "reorgannize" + str(cell) + ".xlsx"

    all_files = glob.glob(os.path.join(target_dir, "*" + str(cell) + ".txt"))
    all_data_files = glob.glob(os.path.join(target_dir,  "*" + str(cell) + "data.txt"))
    all_dark_files = glob.glob(os.path.join(target_dir,  "*dark*.txt"))

    valid_files = set(all_files) - set(all_data_files) - set(all_dark_files)
    valid_files = list(valid_files)
    intensity_ls = [float(os.path.basename(intensity).split("_")[0]) for intensity in valid_files]
    intensity_ls, valid_files = zip(*sorted(zip(intensity_ls, valid_files)))
    excel_sheets = {}
    for file in valid_files:
        df = pd.read_csv(file, delimiter="\t")
        intensity = os.path.basename(file).split("_")[0]
        excel_sheets[intensity] = df
        df.rename(columns={df.columns[0]:"x" + str(intensity),
                          df.columns[1]:"y" + str(intensity)},
                 inplace=True)

    df_tmp = pd.DataFrame()
    for intensity, file in excel_sheets.items():
        df_tmp = pd.concat([df_tmp, file], axis=1)

    if not os.path.isfile(out_summary_file) or cell == 1:
        with pd.ExcelWriter(out_summary_file) as writer:
            # for intensity, file in excel_sheets.items():
            df_tmp.to_excel(writer, sheet_name=str(cell))
        # with pd.ExcelWriter(out_summary_file, engine="openpyxl", mode='a') as writer:
        #     file.to_excel(writer, sheet_name= str(cell))

