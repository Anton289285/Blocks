import datetime

class Some_record():

    def __init__(self, some_file):
        self.rec_file = some_file
        record_file = open(self.rec_file, 'r')
        self.time = record_file.readline()
        self.recordsman = record_file.readline()
        temp_string = self.recordsman.replace('\n', '')
        self.recordsman = temp_string
        self.apple = int(record_file.readline())
        record_file.close()

    def read(self):
        record_file = open(self.rec_file, 'r')
        self.time = record_file.readline()
        self.recordsman = record_file.readline()
        temp_string = self.recordsman.replace('\n', '')
        self.recordsman = temp_string
        self.apple = int(record_file.readline())
        record_file.close()

    def update(self, some_name, some_quantity_apple):
        record_file = open(self.rec_file, 'w')
        self.time = datetime.datetime.now()
        self.time = self.time.ctime()
        record_file.write(self.time + '\n')
        self.recordsman = some_name
        record_file.write(self.recordsman + '\n' )
        self.apple = some_quantity_apple
        record_file.write(str(self.apple) + '\n')
        record_file.close()
