import pandas as pd
class sales:
    def read_data(self):
        d=r"C:\Users\sindh\Downloads\50000 Sales Records.csv"
        df = pd.read_csv(d)
        return df
    def transform_data(self):
        pass
    def extract_data(self):
        pass
    def load_data(self):
        pass

    def region_wise(self, df):
        regionwise_df = df[df['Region'].str.contains(input("Please Enter Region :"))]
        option = input("Do you want to save Data - yes/no :")
        save_data = "yes" or "Yes" or "YES"
        read_data = "no" or "No" or "NO"

        if option == save_data:
            print("Please provide file name without any '.csv' extension")
            file_name = input("file name:")
            regionwise_df.to_csv(r"C:\Users\sindh\Downloads\50000 Sales Records.csv")
            print("File Saved Successfully")
        elif option == read_data:
            print("File was not saved")
        else:
            print("Invalid Details")
        return regionwise_df
    def country_wise(self, df):
         country = df[df['Country'].str.contains(input("Please Enter Country :"))]
         option = input("Do you want to save Data - yes/no :")
         save_data = "yes" or "Yes" or "YES"
         read_data = "no" or "No" or "NO"
         if option == save_data:
            print("Please provide file name without any '.csv' extension")
            file_name = input("file name:")
            country.to_csv(r"C:\Users\sindh\Downloads\50000 Sales Records.csv")
            print("File Saved Successfully")
         elif option == read_data:
            print("File was not saved")
         else:
            print("Invalid Details")
         return country
