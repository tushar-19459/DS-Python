from Student import testStudentDS
def Testing():
    std = testStudentDS()
    std.insert("tushar",45)
    std.insert("raj",5)
    std.insert("kunjoor",15)
    std.insert("kishor",50)
    std.insert("karthik",20)
    std.quickSort()
Testing()