{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "3"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 1. Credit card applications\n",
    "<p>Commercial banks receive <em>a lot</em> of applications for credit cards. Many of them get rejected for many reasons, like high loan balances, low income levels, or too many inquiries on an individual's credit report, for example. Manually analyzing these applications is mundane, error-prone, and time-consuming (and time is money!). Luckily, this task can be automated with the power of machine learning and pretty much every commercial bank does so nowadays. In this notebook, we will build an automatic credit card approval predictor using machine learning techniques, just like the real banks do.</p>\n",
    "<p><img src=\"https://assets.datacamp.com/production/project_558/img/credit_card.jpg\" alt=\"Credit card being held in hand\"></p>\n",
    "<p>We'll use the <a href=\"http://archive.ics.uci.edu/ml/datasets/credit+approval\">Credit Card Approval dataset</a> from the UCI Machine Learning Repository. The structure of this notebook is as follows:</p>\n",
    "<ul>\n",
    "<li>First, we will start off by loading and viewing the dataset.</li>\n",
    "<li>We will see that the dataset has a mixture of both numerical and non-numerical features, that it contains values from different ranges, plus that it contains a number of missing entries.</li>\n",
    "<li>We will have to preprocess the dataset to ensure the machine learning model we choose can make good predictions.</li>\n",
    "<li>After our data is in good shape, we will do some exploratory data analysis to build our intuitions.</li>\n",
    "<li>Finally, we will build a machine learning model that can predict if an individual's application for a credit card will be accepted.</li>\n",
    "</ul>\n",
    "<p>First, loading and viewing the dataset. We find that since this data is confidential, the contributor of the dataset has anonymized the feature names.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 284,
   "metadata": {
    "dc": {
     "key": "3"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "      <th>4</th>\n",
       "      <th>5</th>\n",
       "      <th>6</th>\n",
       "      <th>7</th>\n",
       "      <th>8</th>\n",
       "      <th>9</th>\n",
       "      <th>10</th>\n",
       "      <th>11</th>\n",
       "      <th>12</th>\n",
       "      <th>13</th>\n",
       "      <th>14</th>\n",
       "      <th>15</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>b</td>\n",
       "      <td>30.83</td>\n",
       "      <td>0.000</td>\n",
       "      <td>u</td>\n",
       "      <td>g</td>\n",
       "      <td>w</td>\n",
       "      <td>v</td>\n",
       "      <td>1.25</td>\n",
       "      <td>t</td>\n",
       "      <td>t</td>\n",
       "      <td>1</td>\n",
       "      <td>f</td>\n",
       "      <td>g</td>\n",
       "      <td>00202</td>\n",
       "      <td>0</td>\n",
       "      <td>+</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>a</td>\n",
       "      <td>58.67</td>\n",
       "      <td>4.460</td>\n",
       "      <td>u</td>\n",
       "      <td>g</td>\n",
       "      <td>q</td>\n",
       "      <td>h</td>\n",
       "      <td>3.04</td>\n",
       "      <td>t</td>\n",
       "      <td>t</td>\n",
       "      <td>6</td>\n",
       "      <td>f</td>\n",
       "      <td>g</td>\n",
       "      <td>00043</td>\n",
       "      <td>560</td>\n",
       "      <td>+</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>a</td>\n",
       "      <td>24.50</td>\n",
       "      <td>0.500</td>\n",
       "      <td>u</td>\n",
       "      <td>g</td>\n",
       "      <td>q</td>\n",
       "      <td>h</td>\n",
       "      <td>1.50</td>\n",
       "      <td>t</td>\n",
       "      <td>f</td>\n",
       "      <td>0</td>\n",
       "      <td>f</td>\n",
       "      <td>g</td>\n",
       "      <td>00280</td>\n",
       "      <td>824</td>\n",
       "      <td>+</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>b</td>\n",
       "      <td>27.83</td>\n",
       "      <td>1.540</td>\n",
       "      <td>u</td>\n",
       "      <td>g</td>\n",
       "      <td>w</td>\n",
       "      <td>v</td>\n",
       "      <td>3.75</td>\n",
       "      <td>t</td>\n",
       "      <td>t</td>\n",
       "      <td>5</td>\n",
       "      <td>t</td>\n",
       "      <td>g</td>\n",
       "      <td>00100</td>\n",
       "      <td>3</td>\n",
       "      <td>+</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>b</td>\n",
       "      <td>20.17</td>\n",
       "      <td>5.625</td>\n",
       "      <td>u</td>\n",
       "      <td>g</td>\n",
       "      <td>w</td>\n",
       "      <td>v</td>\n",
       "      <td>1.71</td>\n",
       "      <td>t</td>\n",
       "      <td>f</td>\n",
       "      <td>0</td>\n",
       "      <td>f</td>\n",
       "      <td>s</td>\n",
       "      <td>00120</td>\n",
       "      <td>0</td>\n",
       "      <td>+</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  0      1      2  3  4  5  6     7  8  9   10 11 12     13   14 15\n",
       "0  b  30.83  0.000  u  g  w  v  1.25  t  t   1  f  g  00202    0  +\n",
       "1  a  58.67  4.460  u  g  q  h  3.04  t  t   6  f  g  00043  560  +\n",
       "2  a  24.50  0.500  u  g  q  h  1.50  t  f   0  f  g  00280  824  +\n",
       "3  b  27.83  1.540  u  g  w  v  3.75  t  t   5  t  g  00100    3  +\n",
       "4  b  20.17  5.625  u  g  w  v  1.71  t  f   0  f  s  00120    0  +"
      ]
     },
     "execution_count": 284,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Import pandas\n",
    "import pandas as pd\n",
    "\n",
    "# Load dataset\n",
    "cc_apps = pd.read_csv(\"datasets/cc_approvals.data\", header = None)\n",
    "\n",
    "# Inspect data\n",
    "cc_apps.head(5)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "10"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 2. Inspecting the applications\n",
    "<p>The output may appear a bit confusing at its first sight, but let's try to figure out the most important features of a credit card application. The features of this dataset have been anonymized to protect the privacy, but <a href=\"http://rstudio-pubs-static.s3.amazonaws.com/73039_9946de135c0a49daa7a0a9eda4a67a72.html\">this blog</a> gives us a pretty good overview of the probable features. The probable features in a typical credit card application are <code>Gender</code>, <code>Age</code>, <code>Debt</code>, <code>Married</code>, <code>BankCustomer</code>, <code>EducationLevel</code>, <code>Ethnicity</code>, <code>YearsEmployed</code>, <code>PriorDefault</code>, <code>Employed</code>, <code>CreditScore</code>, <code>DriversLicense</code>, <code>Citizen</code>, <code>ZipCode</code>, <code>Income</code> and finally the <code>ApprovalStatus</code>. This gives us a pretty good starting point, and we can map these features with respect to the columns in the output.   </p>\n",
    "<p>As we can see from our first glance at the data, the dataset has a mixture of numerical and non-numerical features. This can be fixed with some preprocessing, but before we do that, let's learn about the dataset a bit more to see if there are other dataset issues that need to be fixed.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 286,
   "metadata": {
    "dc": {
     "key": "10"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "               2           7          10             14\n",
      "count  690.000000  690.000000  690.00000     690.000000\n",
      "mean     4.758725    2.223406    2.40000    1017.385507\n",
      "std      4.978163    3.346513    4.86294    5210.102598\n",
      "min      0.000000    0.000000    0.00000       0.000000\n",
      "25%      1.000000    0.165000    0.00000       0.000000\n",
      "50%      2.750000    1.000000    0.00000       5.000000\n",
      "75%      7.207500    2.625000    3.00000     395.500000\n",
      "max     28.000000   28.500000   67.00000  100000.000000\n",
      "\n",
      "\n",
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 690 entries, 0 to 689\n",
      "Data columns (total 16 columns):\n",
      "0     690 non-null object\n",
      "1     690 non-null object\n",
      "2     690 non-null float64\n",
      "3     690 non-null object\n",
      "4     690 non-null object\n",
      "5     690 non-null object\n",
      "6     690 non-null object\n",
      "7     690 non-null float64\n",
      "8     690 non-null object\n",
      "9     690 non-null object\n",
      "10    690 non-null int64\n",
      "11    690 non-null object\n",
      "12    690 non-null object\n",
      "13    690 non-null object\n",
      "14    690 non-null int64\n",
      "15    690 non-null object\n",
      "dtypes: float64(2), int64(2), object(12)\n",
      "memory usage: 86.3+ KB\n",
      "None\n",
      "\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "      <th>4</th>\n",
       "      <th>5</th>\n",
       "      <th>6</th>\n",
       "      <th>7</th>\n",
       "      <th>8</th>\n",
       "      <th>9</th>\n",
       "      <th>10</th>\n",
       "      <th>11</th>\n",
       "      <th>12</th>\n",
       "      <th>13</th>\n",
       "      <th>14</th>\n",
       "      <th>15</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>673</th>\n",
       "      <td>?</td>\n",
       "      <td>29.50</td>\n",
       "      <td>2.000</td>\n",
       "      <td>y</td>\n",
       "      <td>p</td>\n",
       "      <td>e</td>\n",
       "      <td>h</td>\n",
       "      <td>2.000</td>\n",
       "      <td>f</td>\n",
       "      <td>f</td>\n",
       "      <td>0</td>\n",
       "      <td>f</td>\n",
       "      <td>g</td>\n",
       "      <td>00256</td>\n",
       "      <td>17</td>\n",
       "      <td>-</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>674</th>\n",
       "      <td>a</td>\n",
       "      <td>37.33</td>\n",
       "      <td>2.500</td>\n",
       "      <td>u</td>\n",
       "      <td>g</td>\n",
       "      <td>i</td>\n",
       "      <td>h</td>\n",
       "      <td>0.210</td>\n",
       "      <td>f</td>\n",
       "      <td>f</td>\n",
       "      <td>0</td>\n",
       "      <td>f</td>\n",
       "      <td>g</td>\n",
       "      <td>00260</td>\n",
       "      <td>246</td>\n",
       "      <td>-</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>675</th>\n",
       "      <td>a</td>\n",
       "      <td>41.58</td>\n",
       "      <td>1.040</td>\n",
       "      <td>u</td>\n",
       "      <td>g</td>\n",
       "      <td>aa</td>\n",
       "      <td>v</td>\n",
       "      <td>0.665</td>\n",
       "      <td>f</td>\n",
       "      <td>f</td>\n",
       "      <td>0</td>\n",
       "      <td>f</td>\n",
       "      <td>g</td>\n",
       "      <td>00240</td>\n",
       "      <td>237</td>\n",
       "      <td>-</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>676</th>\n",
       "      <td>a</td>\n",
       "      <td>30.58</td>\n",
       "      <td>10.665</td>\n",
       "      <td>u</td>\n",
       "      <td>g</td>\n",
       "      <td>q</td>\n",
       "      <td>h</td>\n",
       "      <td>0.085</td>\n",
       "      <td>f</td>\n",
       "      <td>t</td>\n",
       "      <td>12</td>\n",
       "      <td>t</td>\n",
       "      <td>g</td>\n",
       "      <td>00129</td>\n",
       "      <td>3</td>\n",
       "      <td>-</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>677</th>\n",
       "      <td>b</td>\n",
       "      <td>19.42</td>\n",
       "      <td>7.250</td>\n",
       "      <td>u</td>\n",
       "      <td>g</td>\n",
       "      <td>m</td>\n",
       "      <td>v</td>\n",
       "      <td>0.040</td>\n",
       "      <td>f</td>\n",
       "      <td>t</td>\n",
       "      <td>1</td>\n",
       "      <td>f</td>\n",
       "      <td>g</td>\n",
       "      <td>00100</td>\n",
       "      <td>1</td>\n",
       "      <td>-</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>678</th>\n",
       "      <td>a</td>\n",
       "      <td>17.92</td>\n",
       "      <td>10.210</td>\n",
       "      <td>u</td>\n",
       "      <td>g</td>\n",
       "      <td>ff</td>\n",
       "      <td>ff</td>\n",
       "      <td>0.000</td>\n",
       "      <td>f</td>\n",
       "      <td>f</td>\n",
       "      <td>0</td>\n",
       "      <td>f</td>\n",
       "      <td>g</td>\n",
       "      <td>00000</td>\n",
       "      <td>50</td>\n",
       "      <td>-</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>679</th>\n",
       "      <td>a</td>\n",
       "      <td>20.08</td>\n",
       "      <td>1.250</td>\n",
       "      <td>u</td>\n",
       "      <td>g</td>\n",
       "      <td>c</td>\n",
       "      <td>v</td>\n",
       "      <td>0.000</td>\n",
       "      <td>f</td>\n",
       "      <td>f</td>\n",
       "      <td>0</td>\n",
       "      <td>f</td>\n",
       "      <td>g</td>\n",
       "      <td>00000</td>\n",
       "      <td>0</td>\n",
       "      <td>-</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>680</th>\n",
       "      <td>b</td>\n",
       "      <td>19.50</td>\n",
       "      <td>0.290</td>\n",
       "      <td>u</td>\n",
       "      <td>g</td>\n",
       "      <td>k</td>\n",
       "      <td>v</td>\n",
       "      <td>0.290</td>\n",
       "      <td>f</td>\n",
       "      <td>f</td>\n",
       "      <td>0</td>\n",
       "      <td>f</td>\n",
       "      <td>g</td>\n",
       "      <td>00280</td>\n",
       "      <td>364</td>\n",
       "      <td>-</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>681</th>\n",
       "      <td>b</td>\n",
       "      <td>27.83</td>\n",
       "      <td>1.000</td>\n",
       "      <td>y</td>\n",
       "      <td>p</td>\n",
       "      <td>d</td>\n",
       "      <td>h</td>\n",
       "      <td>3.000</td>\n",
       "      <td>f</td>\n",
       "      <td>f</td>\n",
       "      <td>0</td>\n",
       "      <td>f</td>\n",
       "      <td>g</td>\n",
       "      <td>00176</td>\n",
       "      <td>537</td>\n",
       "      <td>-</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>682</th>\n",
       "      <td>b</td>\n",
       "      <td>17.08</td>\n",
       "      <td>3.290</td>\n",
       "      <td>u</td>\n",
       "      <td>g</td>\n",
       "      <td>i</td>\n",
       "      <td>v</td>\n",
       "      <td>0.335</td>\n",
       "      <td>f</td>\n",
       "      <td>f</td>\n",
       "      <td>0</td>\n",
       "      <td>t</td>\n",
       "      <td>g</td>\n",
       "      <td>00140</td>\n",
       "      <td>2</td>\n",
       "      <td>-</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>683</th>\n",
       "      <td>b</td>\n",
       "      <td>36.42</td>\n",
       "      <td>0.750</td>\n",
       "      <td>y</td>\n",
       "      <td>p</td>\n",
       "      <td>d</td>\n",
       "      <td>v</td>\n",
       "      <td>0.585</td>\n",
       "      <td>f</td>\n",
       "      <td>f</td>\n",
       "      <td>0</td>\n",
       "      <td>f</td>\n",
       "      <td>g</td>\n",
       "      <td>00240</td>\n",
       "      <td>3</td>\n",
       "      <td>-</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>684</th>\n",
       "      <td>b</td>\n",
       "      <td>40.58</td>\n",
       "      <td>3.290</td>\n",
       "      <td>u</td>\n",
       "      <td>g</td>\n",
       "      <td>m</td>\n",
       "      <td>v</td>\n",
       "      <td>3.500</td>\n",
       "      <td>f</td>\n",
       "      <td>f</td>\n",
       "      <td>0</td>\n",
       "      <td>t</td>\n",
       "      <td>s</td>\n",
       "      <td>00400</td>\n",
       "      <td>0</td>\n",
       "      <td>-</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>685</th>\n",
       "      <td>b</td>\n",
       "      <td>21.08</td>\n",
       "      <td>10.085</td>\n",
       "      <td>y</td>\n",
       "      <td>p</td>\n",
       "      <td>e</td>\n",
       "      <td>h</td>\n",
       "      <td>1.250</td>\n",
       "      <td>f</td>\n",
       "      <td>f</td>\n",
       "      <td>0</td>\n",
       "      <td>f</td>\n",
       "      <td>g</td>\n",
       "      <td>00260</td>\n",
       "      <td>0</td>\n",
       "      <td>-</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>686</th>\n",
       "      <td>a</td>\n",
       "      <td>22.67</td>\n",
       "      <td>0.750</td>\n",
       "      <td>u</td>\n",
       "      <td>g</td>\n",
       "      <td>c</td>\n",
       "      <td>v</td>\n",
       "      <td>2.000</td>\n",
       "      <td>f</td>\n",
       "      <td>t</td>\n",
       "      <td>2</td>\n",
       "      <td>t</td>\n",
       "      <td>g</td>\n",
       "      <td>00200</td>\n",
       "      <td>394</td>\n",
       "      <td>-</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>687</th>\n",
       "      <td>a</td>\n",
       "      <td>25.25</td>\n",
       "      <td>13.500</td>\n",
       "      <td>y</td>\n",
       "      <td>p</td>\n",
       "      <td>ff</td>\n",
       "      <td>ff</td>\n",
       "      <td>2.000</td>\n",
       "      <td>f</td>\n",
       "      <td>t</td>\n",
       "      <td>1</td>\n",
       "      <td>t</td>\n",
       "      <td>g</td>\n",
       "      <td>00200</td>\n",
       "      <td>1</td>\n",
       "      <td>-</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>688</th>\n",
       "      <td>b</td>\n",
       "      <td>17.92</td>\n",
       "      <td>0.205</td>\n",
       "      <td>u</td>\n",
       "      <td>g</td>\n",
       "      <td>aa</td>\n",
       "      <td>v</td>\n",
       "      <td>0.040</td>\n",
       "      <td>f</td>\n",
       "      <td>f</td>\n",
       "      <td>0</td>\n",
       "      <td>f</td>\n",
       "      <td>g</td>\n",
       "      <td>00280</td>\n",
       "      <td>750</td>\n",
       "      <td>-</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>689</th>\n",
       "      <td>b</td>\n",
       "      <td>35.00</td>\n",
       "      <td>3.375</td>\n",
       "      <td>u</td>\n",
       "      <td>g</td>\n",
       "      <td>c</td>\n",
       "      <td>h</td>\n",
       "      <td>8.290</td>\n",
       "      <td>f</td>\n",
       "      <td>f</td>\n",
       "      <td>0</td>\n",
       "      <td>t</td>\n",
       "      <td>g</td>\n",
       "      <td>00000</td>\n",
       "      <td>0</td>\n",
       "      <td>-</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    0      1       2  3  4   5   6      7  8  9   10 11 12     13   14 15\n",
       "673  ?  29.50   2.000  y  p   e   h  2.000  f  f   0  f  g  00256   17  -\n",
       "674  a  37.33   2.500  u  g   i   h  0.210  f  f   0  f  g  00260  246  -\n",
       "675  a  41.58   1.040  u  g  aa   v  0.665  f  f   0  f  g  00240  237  -\n",
       "676  a  30.58  10.665  u  g   q   h  0.085  f  t  12  t  g  00129    3  -\n",
       "677  b  19.42   7.250  u  g   m   v  0.040  f  t   1  f  g  00100    1  -\n",
       "678  a  17.92  10.210  u  g  ff  ff  0.000  f  f   0  f  g  00000   50  -\n",
       "679  a  20.08   1.250  u  g   c   v  0.000  f  f   0  f  g  00000    0  -\n",
       "680  b  19.50   0.290  u  g   k   v  0.290  f  f   0  f  g  00280  364  -\n",
       "681  b  27.83   1.000  y  p   d   h  3.000  f  f   0  f  g  00176  537  -\n",
       "682  b  17.08   3.290  u  g   i   v  0.335  f  f   0  t  g  00140    2  -\n",
       "683  b  36.42   0.750  y  p   d   v  0.585  f  f   0  f  g  00240    3  -\n",
       "684  b  40.58   3.290  u  g   m   v  3.500  f  f   0  t  s  00400    0  -\n",
       "685  b  21.08  10.085  y  p   e   h  1.250  f  f   0  f  g  00260    0  -\n",
       "686  a  22.67   0.750  u  g   c   v  2.000  f  t   2  t  g  00200  394  -\n",
       "687  a  25.25  13.500  y  p  ff  ff  2.000  f  t   1  t  g  00200    1  -\n",
       "688  b  17.92   0.205  u  g  aa   v  0.040  f  f   0  f  g  00280  750  -\n",
       "689  b  35.00   3.375  u  g   c   h  8.290  f  f   0  t  g  00000    0  -"
      ]
     },
     "execution_count": 286,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Print summary statistics\n",
    "cc_apps_description = cc_apps.describe()\n",
    "print(cc_apps_description)\n",
    "\n",
    "print(\"\\n\")\n",
    "\n",
    "# Print DataFrame information\n",
    "cc_apps_info = cc_apps.info()\n",
    "print(cc_apps_info)\n",
    "\n",
    "print(\"\\n\")\n",
    "\n",
    "# Inspect missing values in the dataset\n",
    "cc_apps.tail(17)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "17"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 3. Handling the missing values (part i)\n",
    "<p>We've uncovered some issues that will affect the performance of our machine learning model(s) if they go unchanged:</p>\n",
    "<ul>\n",
    "<li>Our dataset contains both numeric and non-numeric data (specifically data that are of <code>float64</code>, <code>int64</code> and <code>object</code> types). Specifically, the features 2, 7, 10 and 14 contain numeric values (of types float64, float64, int64 and int64 respectively) and all the other features contain non-numeric values.</li>\n",
    "<li>The dataset also contains values from several ranges. Some features have a value range of 0 - 28, some have a range of 2 - 67, and some have a range of 1017 - 100000. Apart from these, we can get useful statistical information (like <code>mean</code>, <code>max</code>, and <code>min</code>) about the features that have numerical values. </li>\n",
    "<li>Finally, the dataset has missing values, which we'll take care of in this task. The missing values in the dataset are labeled with '?', which can be seen in the last cell's output.</li>\n",
    "</ul>\n",
    "<p>Now, let's temporarily replace these missing value question marks with NaN.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 288,
   "metadata": {
    "dc": {
     "key": "17"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      0      1       2  3  4   5   6      7  8  9   10 11 12     13   14 15\n",
      "673  NaN  29.50   2.000  y  p   e   h  2.000  f  f   0  f  g  00256   17  -\n",
      "674    a  37.33   2.500  u  g   i   h  0.210  f  f   0  f  g  00260  246  -\n",
      "675    a  41.58   1.040  u  g  aa   v  0.665  f  f   0  f  g  00240  237  -\n",
      "676    a  30.58  10.665  u  g   q   h  0.085  f  t  12  t  g  00129    3  -\n",
      "677    b  19.42   7.250  u  g   m   v  0.040  f  t   1  f  g  00100    1  -\n",
      "678    a  17.92  10.210  u  g  ff  ff  0.000  f  f   0  f  g  00000   50  -\n",
      "679    a  20.08   1.250  u  g   c   v  0.000  f  f   0  f  g  00000    0  -\n",
      "680    b  19.50   0.290  u  g   k   v  0.290  f  f   0  f  g  00280  364  -\n",
      "681    b  27.83   1.000  y  p   d   h  3.000  f  f   0  f  g  00176  537  -\n",
      "682    b  17.08   3.290  u  g   i   v  0.335  f  f   0  t  g  00140    2  -\n",
      "683    b  36.42   0.750  y  p   d   v  0.585  f  f   0  f  g  00240    3  -\n",
      "684    b  40.58   3.290  u  g   m   v  3.500  f  f   0  t  s  00400    0  -\n",
      "685    b  21.08  10.085  y  p   e   h  1.250  f  f   0  f  g  00260    0  -\n",
      "686    a  22.67   0.750  u  g   c   v  2.000  f  t   2  t  g  00200  394  -\n",
      "687    a  25.25  13.500  y  p  ff  ff  2.000  f  t   1  t  g  00200    1  -\n",
      "688    b  17.92   0.205  u  g  aa   v  0.040  f  f   0  f  g  00280  750  -\n",
      "689    b  35.00   3.375  u  g   c   h  8.290  f  f   0  t  g  00000    0  -\n"
     ]
    }
   ],
   "source": [
    "# Import numpy\n",
    "import numpy as np\n",
    "\n",
    "# Inspect missing values in the dataset\n",
    "#print(cc_apps.tail(17))\n",
    "\n",
    "# Replace the '?'s with NaN\n",
    "cc_apps = cc_apps.replace('?', np.NaN)\n",
    "\n",
    "# Inspect the missing values again\n",
    "print(cc_apps.tail(17))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "24"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 4. Handling the missing values (part ii)\n",
    "<p>We replaced all the question marks with NaNs. This is going to help us in the next missing value treatment that we are going to perform.</p>\n",
    "<p>An important question that gets raised here is <em>why are we giving so much importance to missing values</em>? Can't they be just ignored? Ignoring missing values can affect the performance of a machine learning model heavily. While ignoring the missing values our machine learning model may miss out on information about the dataset that may be useful for its training. Then, there are many models which cannot handle missing values implicitly such as LDA. </p>\n",
    "<p>So, to avoid this problem, we are going to impute the missing values with a strategy called mean imputation.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 290,
   "metadata": {
    "dc": {
     "key": "24"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      0      1       2  3  4   5   6      7  8  9   10 11 12     13   14 15\n",
      "673  NaN  29.50   2.000  y  p   e   h  2.000  f  f   0  f  g  00256   17  -\n",
      "674    a  37.33   2.500  u  g   i   h  0.210  f  f   0  f  g  00260  246  -\n",
      "675    a  41.58   1.040  u  g  aa   v  0.665  f  f   0  f  g  00240  237  -\n",
      "676    a  30.58  10.665  u  g   q   h  0.085  f  t  12  t  g  00129    3  -\n",
      "677    b  19.42   7.250  u  g   m   v  0.040  f  t   1  f  g  00100    1  -\n",
      "678    a  17.92  10.210  u  g  ff  ff  0.000  f  f   0  f  g  00000   50  -\n",
      "679    a  20.08   1.250  u  g   c   v  0.000  f  f   0  f  g  00000    0  -\n",
      "680    b  19.50   0.290  u  g   k   v  0.290  f  f   0  f  g  00280  364  -\n",
      "681    b  27.83   1.000  y  p   d   h  3.000  f  f   0  f  g  00176  537  -\n",
      "682    b  17.08   3.290  u  g   i   v  0.335  f  f   0  t  g  00140    2  -\n",
      "683    b  36.42   0.750  y  p   d   v  0.585  f  f   0  f  g  00240    3  -\n",
      "684    b  40.58   3.290  u  g   m   v  3.500  f  f   0  t  s  00400    0  -\n",
      "685    b  21.08  10.085  y  p   e   h  1.250  f  f   0  f  g  00260    0  -\n",
      "686    a  22.67   0.750  u  g   c   v  2.000  f  t   2  t  g  00200  394  -\n",
      "687    a  25.25  13.500  y  p  ff  ff  2.000  f  t   1  t  g  00200    1  -\n",
      "688    b  17.92   0.205  u  g  aa   v  0.040  f  f   0  f  g  00280  750  -\n",
      "689    b  35.00   3.375  u  g   c   h  8.290  f  f   0  t  g  00000    0  -\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "0     12\n",
       "1     12\n",
       "2      0\n",
       "3      6\n",
       "4      6\n",
       "5      9\n",
       "6      9\n",
       "7      0\n",
       "8      0\n",
       "9      0\n",
       "10     0\n",
       "11     0\n",
       "12     0\n",
       "13    13\n",
       "14     0\n",
       "15     0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 290,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Impute the missing values with mean imputation\n",
    "cc_apps.fillna(cc_apps.mean(), inplace=True)\n",
    "print(cc_apps.tail(17))\n",
    "\n",
    "# Count the number of NaNs in the dataset to verify\n",
    "cc_apps.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "31"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 5. Handling the missing values (part iii)\n",
    "<p>We have successfully taken care of the missing values present in the numeric columns. There are still some missing values to be imputed for columns 0, 1, 3, 4, 5, 6 and 13. All of these columns contain non-numeric data and this why the mean imputation strategy would not work here. This needs a different treatment. </p>\n",
    "<p>We are going to impute these missing values with the most frequent values as present in the respective columns. This is <a href=\"https://www.datacamp.com/community/tutorials/categorical-data\">good practice</a> when it comes to imputing missing values for categorical data in general.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 292,
   "metadata": {
    "dc": {
     "key": "31"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0     0\n",
      "1     0\n",
      "2     0\n",
      "3     0\n",
      "4     0\n",
      "5     0\n",
      "6     0\n",
      "7     0\n",
      "8     0\n",
      "9     0\n",
      "10    0\n",
      "11    0\n",
      "12    0\n",
      "13    0\n",
      "14    0\n",
      "15    0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# Iterate over each column of cc_apps\n",
    "for col in cc_apps:\n",
    "    # Check if the column is of object type\n",
    "    if cc_apps[col].dtypes == 'object':\n",
    "        # Impute with the most frequent value\n",
    "        cc_apps = cc_apps.fillna(cc_apps[col].value_counts().index[0])\n",
    "\n",
    "# Count the number of NaNs in the dataset and print the counts to verify\n",
    "print(cc_apps.isnull().sum())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "38"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 6. Preprocessing the data (part i)\n",
    "<p>The missing values are now successfully handled.</p>\n",
    "<p>There is still some minor but essential data preprocessing needed before we proceed towards building our machine learning model. We are going to divide these remaining preprocessing steps into three main tasks:</p>\n",
    "<ol>\n",
    "<li>Convert the non-numeric data into numeric.</li>\n",
    "<li>Split the data into train and test sets. </li>\n",
    "<li>Scale the feature values to a uniform range.</li>\n",
    "</ol>\n",
    "<p>First, we will be converting all the non-numeric values into numeric ones. We do this because not only it results in a faster computation but also many machine learning models (like XGBoost) (and especially the ones developed using scikit-learn) require the data to be in a strictly numeric format. We will do this by using a technique called <a href=\"http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html\">label encoding</a>.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 294,
   "metadata": {
    "dc": {
     "key": "38"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [],
   "source": [
    "# Import LabelEncoder\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "\n",
    "# Instantiate LabelEncoder\n",
    "le = LabelEncoder()\n",
    "\n",
    "# Iterate over all the values of each column and extract their dtypes\n",
    "for col in cc_apps:\n",
    "    # Compare if the dtype is object\n",
    "    if cc_apps[col].dtypes =='object':\n",
    "    # Use LabelEncoder to do the numeric transformation\n",
    "        cc_apps[col]=le.fit_transform(cc_apps[col].astype(str))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "45"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 7. Splitting the dataset into train and test sets\n",
    "<p>We have successfully converted all the non-numeric values to numeric ones.</p>\n",
    "<p>Now, we will split our data into train set and test set to prepare our data for two different phases of machine learning modeling: training and testing. Ideally, no information from the test data should be used to scale the training data or should be used to direct the training process of a machine learning model. Hence, we first split the data and then apply the scaling.</p>\n",
    "<p>Also, features like <code>DriversLicense</code> and <code>ZipCode</code> are not as important as the other features in the dataset for predicting credit card approvals. We should drop them to design our machine learning model with the best set of features. In Data Science literature, this is often referred to as <em>feature selection</em>. </p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 296,
   "metadata": {
    "dc": {
     "key": "45"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [],
   "source": [
    "# Import train_test_split\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "# Drop the features 11 and 13 and convert the DataFrame to a NumPy array\n",
    "cc_apps = cc_apps.drop([11,13], axis=1)\n",
    "cc_apps = cc_apps.values\n",
    "\n",
    "# Segregate features and labels into separate variables\n",
    "X,y = cc_apps[:,0:12] , cc_apps[:,13]\n",
    "\n",
    "# Split into train and test sets\n",
    "X_train, X_test, y_train, y_test = train_test_split(X,\n",
    "                                y,\n",
    "                                test_size= 0.33,\n",
    "                                random_state= 42)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "52"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 8. Preprocessing the data (part ii)\n",
    "<p>The data is now split into two separate sets - train and test sets respectively. We are only left with one final preprocessing step of scaling before we can fit a machine learning model to the data. </p>\n",
    "<p>Now, let's try to understand what these scaled values mean in the real world. Let's use <code>CreditScore</code> as an example. The credit score of a person is their creditworthiness based on their credit history. The higher this number, the more financially trustworthy a person is considered to be. So, a <code>CreditScore</code> of 1 is the highest since we're rescaling all the values to the range of 0-1.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 298,
   "metadata": {
    "dc": {
     "key": "52"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [],
   "source": [
    "# Importing the required modules\n",
    "from sklearn.preprocessing import MinMaxScaler\n",
    "\n",
    "# Instantiate the MinMaxScaler with required parameters\n",
    "scaler = MinMaxScaler(feature_range = (0,1))\n",
    "\n",
    "# Rescaling the required arrays\n",
    "rescaledX_train = scaler.fit_transform(X_train)\n",
    "rescaledX_test = scaler.fit_transform(X_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "59"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 9. Fitting a logistic regression model to the train set\n",
    "<p>Essentially, predicting if a credit card application will be approved or not is a <a href=\"https://en.wikipedia.org/wiki/Statistical_classification\">classification</a> task. <a href=\"http://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.names\">According to UCI</a>, our dataset contains more instances that correspond to \"Denied\" status than instances corresponding to \"Approved\" status. Specifically, out of 690 instances, there are 383 (55.5%) applications that got denied and 307 (44.5%) applications that got approved. </p>\n",
    "<p>This gives us a benchmark. A good machine learning model should be able to accurately predict the status of the applications with respect to these statistics.</p>\n",
    "<p>Which model should we pick? A question to ask is: <em>are the features that affect the credit card approval decision process correlated with each other?</em> Although we can measure correlation, that is outside the scope of this notebook, so we'll rely on our intuition that they indeed are correlated for now. Because of this correlation, we'll take advantage of the fact that generalized linear models perform well in these cases. Let's start our machine learning modeling with a Logistic Regression model (a generalized linear model).</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 300,
   "metadata": {
    "dc": {
     "key": "59"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
       "          intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,\n",
       "          penalty='l2', random_state=None, solver='liblinear', tol=0.0001,\n",
       "          verbose=0, warm_start=False)"
      ]
     },
     "execution_count": 300,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Import LogisticRegression\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "\n",
    "# Instantiate a LogisticRegression classifier with default parameter values\n",
    "logreg = LogisticRegression()\n",
    "\n",
    "# Fit logreg to the train set\n",
    "logreg.fit(rescaledX_train, y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "66"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 10. Making predictions and evaluating performance\n",
    "<p>But how well does our model perform? </p>\n",
    "<p>We will now evaluate our model on the test set with respect to <a href=\"https://developers.google.com/machine-learning/crash-course/classification/accuracy\">classification accuracy</a>. But we will also take a look the model's <a href=\"http://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/\">confusion matrix</a>. In the case of predicting credit card applications, it is equally important to see if our machine learning model is able to predict the approval status of the applications as denied that originally got denied. If our model is not performing well in this aspect, then it might end up approving the application that should have been approved. The confusion matrix helps us to view our model's performance from these aspects.  </p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 302,
   "metadata": {
    "dc": {
     "key": "66"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy of logistic regression classifier:  0.8377192982456141\n",
      "[[92 11]\n",
      " [26 99]]\n"
     ]
    }
   ],
   "source": [
    "# Import confusion_matrix\n",
    "from sklearn.metrics import confusion_matrix\n",
    "\n",
    "# Use logreg to predict instances from the test set and store it\n",
    "y_pred = logreg.predict(rescaledX_test)\n",
    "\n",
    "# Get the accuracy score of logreg model and print it\n",
    "print(\"Accuracy of logistic regression classifier: \", logreg.score(rescaledX_test,\n",
    "                                                                  y_test))\n",
    "\n",
    "# Print the confusion matrix of the logreg model\n",
    "print(confusion_matrix(y_test, y_pred))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "73"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 11. Grid searching and making the model perform better\n",
    "<p>Our model was pretty good! It was able to yield an accuracy score of almost 84%.</p>\n",
    "<p>For the confusion matrix, the first element of the of the first row of the confusion matrix denotes the true negatives meaning the number of negative instances (denied applications) predicted by the model correctly. And the last element of the second row of the confusion matrix denotes the true positives meaning the number of positive instances (approved applications) predicted by the model correctly.</p>\n",
    "<p>Let's see if we can do better. We can perform a <a href=\"https://machinelearningmastery.com/how-to-tune-algorithm-parameters-with-scikit-learn/\">grid search</a> of the model parameters to improve the model's ability to predict credit card approvals.</p>\n",
    "<p><a href=\"http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html\">scikit-learn's implementation of logistic regression</a> consists of different hyperparameters but we will grid search over the following two:</p>\n",
    "<ul>\n",
    "<li>tol</li>\n",
    "<li>max_iter</li>\n",
    "</ul>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 304,
   "metadata": {
    "dc": {
     "key": "73"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [],
   "source": [
    "# Import GridSearchCV\n",
    "from sklearn.model_selection import GridSearchCV\n",
    "\n",
    "# Define the grid of values for tol and max_iter\n",
    "tol = [0.01, 0.001, 0.0001]\n",
    "max_iter = [100,150,200]\n",
    "\n",
    "# Create a dictionary where tol and max_iter are keys and the lists of their values are corresponding values\n",
    "param_grid = dict({'tol':tol,'max_iter':max_iter})"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "80"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 12. Finding the best performing model\n",
    "<p>We have defined the grid of hyperparameter values and converted them into a single dictionary format which <code>GridSearchCV()</code> expects as one of its parameters. Now, we will begin the grid search to see which values perform best.</p>\n",
    "<p>We will instantiate <code>GridSearchCV()</code> with our earlier <code>logreg</code> model with all the data we have. Instead of passing train and test sets separately, we will supply <code>X</code> (scaled version) and <code>y</code>. We will also instruct <code>GridSearchCV()</code> to perform a <a href=\"https://www.dataschool.io/machine-learning-with-scikit-learn/\">cross-validation</a> of five folds.</p>\n",
    "<p>We'll end the notebook by storing the best-achieved score and the respective best parameters.</p>\n",
    "<p>While building this credit card predictor, we tackled some of the most widely-known preprocessing steps such as <strong>scaling</strong>, <strong>label encoding</strong>, and <strong>missing value imputation</strong>. We finished with some <strong>machine learning</strong> to predict if a person's application for a credit card would get approved or not given some information about that person.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 317,
   "metadata": {
    "dc": {
     "key": "80"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [],
   "source": [
    "# Instantiate GridSearchCV with the required parameters\n",
    "grid_model = GridSearchCV(estimator= logreg, param_grid= param_grid, cv= 5)\n",
    "\n",
    "# Use scaler to rescale X and assign it to rescaledX\n",
    "rescaledX = scaler.fit_transform(X)\n",
    "\n",
    "# Fit data to grid_model\n",
    "grid_model_result = grid_model.fit(rescaledX, y)\n",
    "\n",
    "# Summarize results\n",
    "best_score = grid_model_result.best_score_\n",
    "best_params = grid_model_result.best_params_\n",
    "#print(\"Best: %f using %s\" % (..., ...))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
