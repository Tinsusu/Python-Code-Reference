class AnomalyData:
    """This class read in data from text file"""
    data = {}
    decade_dict = {}
    def __init__(self, filename: str, year_range=(0,9999)):
        """ function  compiles this filter_re_str into a regular expression,
            and then use this regular expression to search in each
            line whether it can find a match of the regular expression in the line
            :param filename and year range
            :return: the function  returns a dictionary """
        self.filename = filename
        self.year_range = year_range
        file = open(filename, "r")
        list_of_lines = file.readlines()
        file.close()
        data_listt = []
        for line in list_of_lines:
            if line[0] == "%":
                continue
            else:
                line = line.strip("\n")
                if len(line) > 1:
                    data_listt.append(line)
        data_list2 = []
        i = 0
        #  for index, line in enumerate(data_listt):
        for i in range(0, len(data_listt)):
            if year_range[0] <= int(data_listt[i][:6]) < year_range[1]:
                data_list2.append(data_listt[i])
            else:
                continue
        keep_list = []
        for text in data_list2:
            splitt = text.split(' ')
            x = []
            for i in splitt:
                if len(i) > 0:
                    x.append(i)
                    list(x)
            keep_list.append(x)
        # return (keep_list)
        key = []
        value = []
        for text in keep_list:
            # text = text.split('-')
            key.append(int(text[0]))
            text.pop(0)  # pop out the year I dont want it in the value.
            value.append([float(x) for x in text])  # Change string into float
            d1 = zip(key, value)
            AnomalyData.data.update((dict(d1)))

    def one_value_per_decade(self):
        """This method should create a new local dictionary variable."""
        year_list = []
        lodict = {}
        for year in AnomalyData.data.keys():
            if int(year) % 10 == 0:
                year_list.append(year)
        for key, value in AnomalyData.data.items():
            if key in year_list:
                lodict.update({key:value})
        return lodict

#anomaly_data = AnomalyData('Land_and_Ocean_summary.txt')
#value1 = anomaly_data.data[1990][0]
#value = anomaly_data.one_value_per_decade()
#print(value1)
#print(value)

 #   def one_value_per_decade ():