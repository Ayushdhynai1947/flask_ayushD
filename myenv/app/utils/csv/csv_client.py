import csv


class CsvClient:
    def __init__(self,file_path=None,sheet_name= None) -> None:
        self.file_path = file_path
        self.sheet_name =sheet_name
        
        
    def read(self):
        try :
            with open("file open ",'r') as file :
            reader = csv.DictReader(file)
            data =[]
            for row in reader:
                data.append(row)
            return data
        except FileNotFoundError:
            print(f"File not found:{self.file_path}")
        except Exception as e:
            print(f"An error occured:{str(e)}")
                