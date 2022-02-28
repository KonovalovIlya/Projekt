class Date:
    def __init__(self, day = 0, month = 0, year = 0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date : str) -> 'Date':
        day, month, year = map(int, date.split('-'))
        date_obj = cls(day, month, year)
        return date_obj

    @classmethod
    def is_date_valid(cls, date : str):
        if int(date.split('-')[0]) > 31 and date.split('-')[1] in ['01', '03', '05', '07', '08', '10', '12'] or\
            int(date.split('-')[0]) > 30 and date.split('-')[1] in ['04', '06', '09', '11'] or\
            int(date.split('-')[0]) > 28 and date.split('-')[1] == '02' or\
            int(date.split('-')[1]) > 12 or\
            len(date.split('-')[2]) != 4:
            return False
        else:
            return True

    def __str__(self) -> str:
        return 'День: {}\tМесяц: {}\tГод: {}'.format(self.day, self.month, self.year)




date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))