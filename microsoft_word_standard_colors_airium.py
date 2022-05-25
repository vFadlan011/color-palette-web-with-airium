from airium import Airium
import pandas as pd

df_path = "microsoft_word_standard_colors_data.csv"
df = pd.read_csv( df_path, sep=';')

# select BW columns
df_bw = df['BW']

# select color columns
df_c = df.drop(columns='BW')
# Get list of columns name
cgroups = df_c.columns
# Remove row with index higher than 6
df_c.drop(df_c[df_c.index > 6].index, inplace=True)

#Airium
a = Airium()

""" 
VARIABLE GUIDE

df = DataFrame
c = color
bw = black n white / grayscale
bg = background

cgroup = color group
cgroup.head class:
    cname = colorname
    texthd = text head
    bgcolhd = background color head

cgroup.gradation class:
    grad = gradation
    textcol = text color *color code used as text color
    bgcol = background color *color code used as background color
    textwithbgcol = text with background color *color code used as text color, and inversed color code used as background color
"""

# create <html> tag
with a.html(lang="en"):
    # create <head>
    with a.head():
        a.meta(charset="utf-8")
        a.title(_t="Microsoft Word Standard Colors")
        a.link(rel="stylesheet", href="style.css")
    # create <body>
    with a.body():
        # GRAYSCALE GROUP
        with a.div(klass="BW"):
            with a.div(klass="cgroup"):
                # GROUP HEAD
                    #   contains group name, avg color as text, avg color as bg
                with a.div(klass="head"):
                    # Group name
                    with a.div(klass="CName"):
                        with a.h3():
                            a("GRAYSCALE")
                    # Avg color as text
                    with a.div(klass="texthd"):
                        with a.h3(style="color:#{0};".format(df_bw[17])):
                            a("#{0}".format(df_bw[17]))
                    # Avg color as bg
                    with a.div(klass="bgcolhd", style="background-color:#{};".format(df_bw[17])):
                        pass
                
                # GRADATION
                #   create "col"(colors) class from df_bw[index]
                for i in range(0, 17):
                    # inverse i
                    j = 16-i
                    with a.div(klass="grad", style="background-color:#{0};".format(df_bw[17])):
                        # as text
                        with a.div(klass="textcol", style="color:#{};".format(df_bw[i])):
                            with a.h4():
                                a("#{0}".format(df_bw[i]))
                        # as background
                        with a.div(klass="bgcol", style="background-color:#{0};".format(df_bw[i])):
                            pass
                        #as text with inverted background
                        with a.div(klass="textwithbgcol", style="background-color:#{0}; color:#{1};".format(df_bw[j], df_bw[i])):
                            with a.h4():
                                a("#{0}".format(df_bw[i]))
                

        # COLOR GROUP
        with a.div(klass="COLORS"):
            # CREATE "cgroup" from dataframe cols
            for groupid in cgroups:
                with a.div(klass="cgroup"):
                    # GROUP HEAD
                    #   contains group name, avg color as text, avg color as bg
                    with a.div(klass="head"):
                        # Group name
                        with a.div(klass="CName"):
                            with a.h3():
                                a(groupid)
                        # Avg color as text
                        with a.div(klass="texthd"):
                            with a.h3(style="color:#{}".format(df_c[groupid][6])):
                                a('#{}'.format(df_c[groupid][6]))
                        # Avg color as bg
                        with a.div(klass="bgcolhd", style="background-color:#{}".format(df_c[groupid][6])):
                            pass

                    # GRADATION
                    #   create "col"(colors) class from df_c[groupid][index]
                    for i in range(0,6):
                        #inverse i
                        j = 5-i
                        with a.div(klass="grad", style="background-color:#{0};".format(df_c[groupid][6])):
                            # as text
                            with a.div(klass="textcol", style="color:#{0};".format(df_c[groupid][i])):
                                with a.h4():
                                    a("#{0}".format(df_c[groupid][i]))
                            # as background
                            with a.div(klass="bgcol", style="background-color:#{0};".format(df_c[groupid][i])):
                                pass
                            # as text with inverted background
                            with a.div(klass="textwithbgcol", style="background-color:#{0}; color:#{1};".format(df_c[groupid][j], df_c[groupid][i])):
                                with a.h4():
                                    a("#{0}".format(df_c[groupid][i]))


# SAVE HTML FILE
html_path = "microsoft_word_standard_colors_airium.html"
html = str(a)

with open(html_path, 'wb') as f:
    f.write(bytes(html, encoding='utf8'))