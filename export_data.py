class ExportData():
    def __init__(self, dataFrame, export_to='json'):
        if export_to in ['json', 'csv', 'xlsx']:
            self.export_to = export_to
        else:
            print("cannot export to", export_to, 'file')
            return
        self.path = 'data/job data.'
        self.df = dataFrame
        self.initialize()

    def initialize(self):
        if self.export_to == 'json':
            self.export_to_json()
        elif self.export_to == 'csv':
            self.export_to_csv()
        else:
            self.export_to_xlsx()

    def export_to_json(self):
        path = self.path + 'json'
        self.df.to_json(path, orient='records', lines=False, indent=4)

    def export_to_csv(self):
        pass

    def export_to_xlsx(self):
        pass
