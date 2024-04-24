
# Rpository Structure:
```
- 📦 MultiNet Route Optimizer
  |- 📄 README.md        #Guide file
  |- 📂 Notebooks        #Here you can see a All_in_one.ipynb which is the main file. You can run it on Google Colab.
  |- 📂 Report           #Here you can see a pdf presentation file to clarification
    |-- 📂 CSV files     #Here you can see the results of jupyter file.
  |- 📂 Src              #Here you can see random_generator.py which has generated random_generator.csv file.
  |- 📂 Topologies       #Here you can see two used topologies in the program
```
# Guide to use:
Just run All_in_one.ipynb on colab.

# Project Detail

**Problem**: Routing strategies for multilayer network
planning.

**Goal**: Addressing the challenge of routing demands generated randomly
in Top-Down and Bottom-Up approach and comparing them using optimizaton methods!


For the problem we must consider the following sections:

| 1_Constraints                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WDM bandwidth    | 4.8 THz in C-band--> Max 96 channels at 50 GHz each                                                                                                                     |
| WDM trail Capacity                                 | 500 Gb/s for 1300 km reach and 400 Gb/s for 2500 km reach |
| Demand Rate                             | 100Gb/s or  200Gb/s                                                                                                                                      |


| 2_Assumptions For National topology                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Number of Nodes    |    8                                                                                                                 |
| Number of links                                 | 16 |
| Average length of link                            | Near 150 Km                                                                                                                                |
| Maximum length of link                            | Near 400 Km                                                                                                                                |

| 3_Assumptions For Continental topology                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Number of Nodes    |    8                                                                                                                 |
| Number of links                                 | 20 |
| Average length of link                            | Near 300 Km                                                                                                                                |
| Maximum length of link                            | Near 1000 Km                                                                                                                                |

| 3_Objectives to compare                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ob1    |    Deployed WDM trails                                                                                                                 |
| Ob2                                 | Filling ratio  |
| Ob3                           | Average fiber occupation                                                                                                                                |


# Download presentation file
if you cannot see pdf file in Report folder, try to use the following link
[Link](https://drive.google.com/file/d/1ZvIotf1deqFiXnZfRrRoocD2ExstaiH7/view?usp=sharing)





