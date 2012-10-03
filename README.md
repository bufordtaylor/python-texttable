python-texttable
================

For easy printing of ascii tables within python

# Installation:

        pip install -U git+http://github.com/bufordtaylor/python-texttable


# Example:

        table = Texttable()
        table.set_cols_align(["l", "r", "c"])
        table.set_cols_valign(["t", "m", "b"])
        table.add_rows([ [get_color_string(bcolors.GREEN, "Name Of Person"), "Age", "Nickname"],
                     ["Mr\nXavier\nHuon", 32, "Xav'"],
                     ["Mr\nBaptiste\nClement", 1, "Baby"] ])
        print table.draw() + "\\n"

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
        print table.draw()

# Result:

        "Name Of Person" is in GREEN, but markdown doesn't seem to support colors, or I don't want to find it

        +----------------+-----+----------+
        | Name Of Person | Age | Nickname |
        +================+=====+==========+
        | Mr             |     |          |
        | Xavier         |  32 |          |
        | Huon           |     |   Xav'   |
        +----------------+-----+----------+
        | Mr             |     |          |
        | Baptiste       |   1 |          |
        | Clement        |     |   Baby   |
        +----------------+-----+----------+

        text   float       exp      int     auto
        ===========================================
        abcd   67.000   6.540e+02   89    128.001
        efgh   67.543   6.540e-01   90    1.280e+22
        ijkl   0.000    5.000e-78   89    0.000
        mnop   0.023    5.000e+78   92    1.280e+22
