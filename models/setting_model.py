class SettingModel:
    def __init__(self, driver, database, multi_process, history, role):
        self.driver = driver
        self.database = database
        self.multi_process = multi_process
        self.history = history
        self.role = role
