import os
import sys


class Properties(object):

    def __init__(self, fileName):
        PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
        self.fileName = PROJECT_ROOT + "/" + fileName
        self.properties = {}

    def __getDict(self, strName, dictName, value):

        if (strName.find('.') > 0):
            k = strName.split('.')[0]
            dictName.setdefault(k, {})
            return self.__getDict(strName[len(k) + 1:], dictName[k], value)
        else:
            dictName[strName] = value
            return

    def getProperties(self):
        try:
            pro_file = open(self.fileName, 'Ur')
            for line in pro_file.readlines():
                line = line.strip().replace('\n', '')
                if line.find("#") != -1:
                    line = line[0:line.find('#')]
                if line.find('=') > 0:
                    strs = line.split('=')
                    strs[1] = line[len(strs[0]) + 1:]
                    self.__getDict(strs[0].strip(), self.properties, strs[1].strip())
        except Exception:
            print("properties file read error.")
        else:
            pro_file.close()

        return self.properties
