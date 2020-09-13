from member import Member

import pandas as pd


class Spreadsheet:
    def __init__(self, filepath=None, url=None):
        assert filepath != None or url != None

        self.csv: pd.DataFrame = None
        self.members:[Member] = []

        if filepath != None:
            self.csv = pd.read_csv(filepath,header=None,index_col=None)
            member_number = int(self.csv.iloc[0][0])
            print(f"found {member_number} members")
            for i in range(member_number):
                self.members.append(Member(self.csv.iloc[1][i]))
                print(f"found {self.members[-1].name}")
        elif url != None:
            raise NotImplementedError
