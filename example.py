from texttable import Texttable, get_color_string, bcolors

table = Texttable()
table.set_cols_align(["l", "r", "c"])
table.set_cols_valign(["t", "m", "b"])
table.add_rows([
    [get_color_string(bcolors.GREEN, "Name Of Person"), "Age", "Nickname"],
     ["Mr\nXavier\nHuon", 32, "Xav'"],
     [get_color_string(bcolors.BLUE,"Mr\nBaptiste\nClement"),
      1,
      get_color_string(bcolors.RED,"Baby")] ])
print(table.draw() + "\n")

table = Texttable()
table.set_deco(Texttable.HEADER)
table.set_cols_dtype(['t',  # text
                      'f',  # float (decimal)
                      'e',  # float (exponent)
                      'i',  # integer
                      'a']) # automatic
table.set_cols_align(["l", "r", "r", "r", "l"])
table.add_rows([["text",    "float", "exp", "int", "auto"],
                ["abcd",    "67",    654,   89,    128.001],
                ["efghijk", 67.5434, .654,  89.6,  12800000000000000000000.00023],
                ["lmn",     5e-78,   5e-78, 89.4,  .000000000000128],
                ["opqrstu", .023,    5e+78, 92.,   12800000000000000000000]])
print(table.draw())
