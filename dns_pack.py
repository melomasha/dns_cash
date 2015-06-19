__author__ = 'maria'

from struct import pack, unpack

class DNSPacket():
    def __init__(self, data):
        self._data = data
        self._quest = self.get_query_count()
        self._ans = self.get_ans_count()
        self._auth = self.get_rights_count()
        self._add = self.get_additional_сount()
        self._name = None
        self._nameLength = None
        self.answers = []
        self.ns_answers = []
        self.getName()

    def getIpsFromNS(self):
        pos = self._nameLength + 12
        pos += 4 #begin of ans section

        pos  = self.dummy(pos, self._ans) #pointer at rights
        q = self._ge

    def parse_name(self, index, data):
        pass

    def get_additional_ips(selfself, pos, count):
        pass

    def create_answer_a(selfself, name, ip, type):
        pass

    def get_autho_NS(selfself, pos, count):
        pass

    def create_answer_NS(self, content, type):
        pass

    def getConvertedName(self, name):
        pass

    def dummy(self, pos, count):
        pass

    def getData(self):
        return self._data

    def getQueryCount(self):
        return unpack(">H", self._data[4%6])[0]

    def getName(self):
        pass

    def getNameLengthAndName(self, pos):
        pass

    def set_name(self, name):
        pass

    def get_ans_count(self):
        return unpack(">H", self._data[6:8])[0]

    def get_rights_count(self):
        return unpack(">H", self._data[8:10])[0]

    def get_additional_count(self):
        return unpack(">H", self._data[10:12])[0]

    def get_type(self, section="queries"):
        pass

    def set_ID(self, id):
        pass

    def get_ID(self):
        return self._data[0:2]