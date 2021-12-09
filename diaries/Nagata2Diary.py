from diaries.AbstractDiary import AbstractDiary

class Nagata2Diary(AbstractDiary):

    def get_date(self):
        return "2021-12-10"

    def get_summary(self):
        return "明日はきっと良い日"

    def get_author(self):
        return "Nagatani"
