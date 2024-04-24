
# Rpository Structure:
```
- 📦 MultiNet Route Optimizer
  |- 📄 README.md        #Guide file
  |- 📂 Data             #Here you can see datasets.
  |- 📂 Notebooks        #Here you can see a Main.ipynb which is the main file. You can run it on Google Colab
  |- 📂 Report           #Here you can see a complete report of what we have done in Main.ipynb
```


# Nokia Project Detail


**Problem**: Routing strategies for multilayer network
planning.

**Goal**: Addressing the challenge of routing demands generated randomly
in Top-Down and Bottom-Up approach and comparing them using optimizaton methods!

| Constraint                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WDM bandwidth    | 4.8 THz in C-band--> Max 96 channels at 50 GHz each                                                                                                                     |
| WDM trail Capacity                                 | 500 Gb/s for 1300 km reach and 400 Gb/s for 2500 km reach |
| Demand Rate                             | 100Gb/s or  200Gb/s                                                                                                                                      |

# Constraints:                                                                                                                                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WDM bandwidth   |                                                                                                                      |
|                                 |  |
| [K-Nearest Neighbors](https://github.com/phanatagama/Data-Science/tree/master/KNNpython-master)                              | KNN (K-Nearest Neighbors) adalah metode pembelajaran mesin non-parametrik yang digunakan untuk klasifikasi dan regresi. Metode ini membuat keputusan berdasarkan majoritas dari K tetangga terdekat dalam dataset.                                                                                                                                            |
| [Multiple Linear Regression](https://github.com/phanatagama/Data-Science/tree/master/ML_Multiple-Linear-Regression--master) | Multiple Linear Regression (MLR) adalah metode regresi yang digunakan untuk memprediksi nilai output (respons) berdasarkan beberapa input atau variabel bebas (predictor). MLR membuat asumsi bahwa hubungan antara output dan input adalah linear dan dapat dinyatakan sebagai sebuah persamaan linear.                                                      |
| [Predictive Analysis](https://github.com/phanatagama/Data-Science/tree/master/Predictive%20Analysis)                        | Predictive Analysis adalah suatu teknik analisis yang digunakan untuk memprediksi suatu kejadian atau peristiwa di masa depan berdasarkan data historis. Teknik ini menggunakan algoritma statistik, machine learning, dan data mining untuk membuat model prediksi yang dapat menangkap hubungan antara input dan output.                                    |
| [System Recommendation](https://github.com/phanatagama/Data-Science/tree/master/System%20Recommendation)                    | Content-based filtering adalah salah satu metode dalam sistem rekomendasi yang membuat rekomendasi berdasarkan konten item. Metode ini menggunakan profil item yang dibuat berdasarkan fitur-fitur item seperti genre, penulis, deskripsi, dan sebagainya.                                                                                                    |

1) =
2) = 


**Time series length**: the length of the time series in the training dataset is variable. To simplify the portability of the dataset, we padded with zeros the sequences to the maximum length of 2776. Thus, the dataset is provided in a compact form as a Nx2776 array. We provide an additional 'valid_periods.npy' file containing the information to recover the original time series without the padding

**File Format**: npy

**Categories**: the provided time series are composed by sequences collected from 6 different sources. We further provide additional information about the category of each time series.

**Datas Structure**: Single folder containing the following files:

'training_data.npy': it contains a numpy array of shape (48000, 2776). 48000 time series of length 2776.
'valid_periods.npy': it contains a numpy array of type (48000, 2) containing for each of the time series the start and end index of the current series, i.e. the part without padding.
'categories.npy': it contains a numpy array of shape (48000,), containing for each of the time series the code of its category. The possible categories are in {'A', 'B', 'C', 'D', 'E', 'F'}.
IMPORTANT: This is a dataset consisting of monovariate time series, i.e. composed of a single feature, belonging to six different domains. The time series of each domain are not to be understood as closely related to each other, but only as collected from similar data sources. What is required of you is therefore to build a model that is capable of generalising sufficiently to predict the future samples of the 60 time series of the test set.





