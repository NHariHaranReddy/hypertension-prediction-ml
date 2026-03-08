{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "h9sQoa6kHDuA"
      },
      "source": [
        "# **DATA COLLECTION**\n",
        "\n",
        "---\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 181,
      "metadata": {
        "id": "AGQBx278CuGL"
      },
      "outputs": [],
      "source": [
        "#importing required libraries\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 182,
      "metadata": {
        "id": "iHK-0kxtC-OI"
      },
      "outputs": [],
      "source": [
        "#loading the datset\n",
        "data = pd.read_csv(\"hypertension_data.csv\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 183,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 313
        },
        "id": "rnZSkGXoDQkR",
        "outputId": "903bf9b2-e9b2-47c4-f355-3ca3563d6177"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "        C    Age History Patient TakeMedication Severity BreathShortness  \\\n",
              "0    Male  18-34     Yes      No             No     Mild              No   \n",
              "1  Female  18-34     Yes      No             No     Mild              No   \n",
              "2    Male  35-50     Yes      No             No     Mild              No   \n",
              "3  Female  35-50     Yes      No             No     Mild              No   \n",
              "4    Male  51-64     Yes      No             No     Mild              No   \n",
              "\n",
              "  VisualChanges NoseBleeding Whendiagnoused   Systolic Diastolic  \\\n",
              "0            No          No         <1 Year  111 - 120   81 - 90   \n",
              "1            No          No         <1 Year  111 - 120   81 - 90   \n",
              "2            No          No         <1 Year  111 - 120   81 - 90   \n",
              "3            No          No         <1 Year  111 - 120   81 - 90   \n",
              "4            No          No         <1 Year  111 - 120   81 - 90   \n",
              "\n",
              "  ControlledDiet                  Stages  \n",
              "0             No  HYPERTENSION (Stage-1)  \n",
              "1             No  HYPERTENSION (Stage-1)  \n",
              "2             No  HYPERTENSION (Stage-1)  \n",
              "3             No  HYPERTENSION (Stage-1)  \n",
              "4             No  HYPERTENSION (Stage-1)  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-fb10973e-998e-4474-b666-c781620474be\" class=\"colab-df-container\">\n",
              "    <div>\n",
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
              "      <th>C</th>\n",
              "      <th>Age</th>\n",
              "      <th>History</th>\n",
              "      <th>Patient</th>\n",
              "      <th>TakeMedication</th>\n",
              "      <th>Severity</th>\n",
              "      <th>BreathShortness</th>\n",
              "      <th>VisualChanges</th>\n",
              "      <th>NoseBleeding</th>\n",
              "      <th>Whendiagnoused</th>\n",
              "      <th>Systolic</th>\n",
              "      <th>Diastolic</th>\n",
              "      <th>ControlledDiet</th>\n",
              "      <th>Stages</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Male</td>\n",
              "      <td>18-34</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Mild</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>&lt;1 Year</td>\n",
              "      <td>111 - 120</td>\n",
              "      <td>81 - 90</td>\n",
              "      <td>No</td>\n",
              "      <td>HYPERTENSION (Stage-1)</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Female</td>\n",
              "      <td>18-34</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Mild</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>&lt;1 Year</td>\n",
              "      <td>111 - 120</td>\n",
              "      <td>81 - 90</td>\n",
              "      <td>No</td>\n",
              "      <td>HYPERTENSION (Stage-1)</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Male</td>\n",
              "      <td>35-50</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Mild</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>&lt;1 Year</td>\n",
              "      <td>111 - 120</td>\n",
              "      <td>81 - 90</td>\n",
              "      <td>No</td>\n",
              "      <td>HYPERTENSION (Stage-1)</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Female</td>\n",
              "      <td>35-50</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Mild</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>&lt;1 Year</td>\n",
              "      <td>111 - 120</td>\n",
              "      <td>81 - 90</td>\n",
              "      <td>No</td>\n",
              "      <td>HYPERTENSION (Stage-1)</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Male</td>\n",
              "      <td>51-64</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Mild</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>&lt;1 Year</td>\n",
              "      <td>111 - 120</td>\n",
              "      <td>81 - 90</td>\n",
              "      <td>No</td>\n",
              "      <td>HYPERTENSION (Stage-1)</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-fb10973e-998e-4474-b666-c781620474be')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-fb10973e-998e-4474-b666-c781620474be button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-fb10973e-998e-4474-b666-c781620474be');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "data",
              "summary": "{\n  \"name\": \"data\",\n  \"rows\": 1825,\n  \"fields\": [\n    {\n      \"column\": \"C\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Female\",\n          \"Male\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Age\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 4,\n        \"samples\": [\n          \"35-50\",\n          \"65+\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"History\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"No\",\n          \"Yes\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Patient\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Yes\",\n          \"No\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"TakeMedication\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 3,\n        \"samples\": [\n          \"No\",\n          \"Yes \"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Severity\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 3,\n        \"samples\": [\n          \"Mild\",\n          \"Sever\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"BreathShortness\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Yes\",\n          \"No\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"VisualChanges\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Yes\",\n          \"No\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"NoseBleeding\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 3,\n        \"samples\": [\n          \"No \",\n          \"No\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Whendiagnoused\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 3,\n        \"samples\": [\n          \"<1 Year\",\n          \"1 - 5 Years\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Systolic\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 5,\n        \"samples\": [\n          \"121- 130\",\n          \"121 - 130\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Diastolic\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 5,\n        \"samples\": [\n          \"91 - 100\",\n          \"70 - 80\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"ControlledDiet\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Yes\",\n          \"No\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Stages\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 6,\n        \"samples\": [\n          \"HYPERTENSION (Stage-1)\",\n          \"HYPERTENSION (Stage-2)\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 183
        }
      ],
      "source": [
        "#previewing the dataset\n",
        "data.head()\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 184,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "30ft9FI1DS-s",
        "outputId": "5c82c489-c060-4144-9c65-eaf278633dd6"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(1825, 14)"
            ]
          },
          "metadata": {},
          "execution_count": 184
        }
      ],
      "source": [
        "#size of the dataset\n",
        "data.shape"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 185,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WrJdgfTfDYvB",
        "outputId": "4ec84df4-f200-4332-bba1-3a15c3512544"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 1825 entries, 0 to 1824\n",
            "Data columns (total 14 columns):\n",
            " #   Column           Non-Null Count  Dtype \n",
            "---  ------           --------------  ----- \n",
            " 0   C                1825 non-null   object\n",
            " 1   Age              1825 non-null   object\n",
            " 2   History          1825 non-null   object\n",
            " 3   Patient          1825 non-null   object\n",
            " 4   TakeMedication   1825 non-null   object\n",
            " 5   Severity         1825 non-null   object\n",
            " 6   BreathShortness  1825 non-null   object\n",
            " 7   VisualChanges    1825 non-null   object\n",
            " 8   NoseBleeding     1825 non-null   object\n",
            " 9   Whendiagnoused   1825 non-null   object\n",
            " 10  Systolic         1825 non-null   object\n",
            " 11  Diastolic        1825 non-null   object\n",
            " 12  ControlledDiet   1825 non-null   object\n",
            " 13  Stages           1825 non-null   object\n",
            "dtypes: object(14)\n",
            "memory usage: 199.7+ KB\n"
          ]
        }
      ],
      "source": [
        "#dataset info\n",
        "data.info()\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zdM0CKwDEPtX"
      },
      "source": [
        "# **DATA PREPARATION**\n",
        "\n",
        "---\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "iVrR9ODLIdN1"
      },
      "source": [
        "**1. Handling Missing Values**\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 186,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 523
        },
        "id": "bz3GbKZFDaiz",
        "outputId": "be88e52d-5723-432f-cbe5-9f063a947db7"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "C                  0\n",
              "Age                0\n",
              "History            0\n",
              "Patient            0\n",
              "TakeMedication     0\n",
              "Severity           0\n",
              "BreathShortness    0\n",
              "VisualChanges      0\n",
              "NoseBleeding       0\n",
              "Whendiagnoused     0\n",
              "Systolic           0\n",
              "Diastolic          0\n",
              "ControlledDiet     0\n",
              "Stages             0\n",
              "dtype: int64"
            ],
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
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>C</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Age</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>History</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Patient</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>TakeMedication</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Severity</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>BreathShortness</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>VisualChanges</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>NoseBleeding</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Whendiagnoused</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Systolic</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Diastolic</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>ControlledDiet</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Stages</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> int64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 186
        }
      ],
      "source": [
        "#checking for missing values\n",
        "data.isnull().sum()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OgLL0Ij7IqGH"
      },
      "source": [
        "**2. Data Type Correction**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 187,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XGXiatJsEgVb",
        "outputId": "a6371f2d-d040-4251-9296-31cc7b2984fc"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['C', 'Age', 'History', 'Patient', 'TakeMedication', 'Severity',\n",
              "       'BreathShortness', 'VisualChanges', 'NoseBleeding', 'Whendiagnoused',\n",
              "       'Systolic', 'Diastolic', 'ControlledDiet', 'Stages'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {},
          "execution_count": 187
        }
      ],
      "source": [
        "#Checking column name\n",
        "data.columns"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 188,
      "metadata": {
        "id": "KdZ2OrfeEt2C"
      },
      "outputs": [],
      "source": [
        "#Renaming the column\n",
        "data.rename(columns={'C':'Gender'}, inplace = True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 189,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0XCD23MpE2V4",
        "outputId": "cccf0952-a611-4fac-d681-263e06123fe9"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['Gender', 'Age', 'History', 'Patient', 'TakeMedication', 'Severity',\n",
              "       'BreathShortness', 'VisualChanges', 'NoseBleeding', 'Whendiagnoused',\n",
              "       'Systolic', 'Diastolic', 'ControlledDiet', 'Stages'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {},
          "execution_count": 189
        }
      ],
      "source": [
        "#Verification\n",
        "data.columns"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "aj2ZlPtSIubK"
      },
      "source": [
        "**3. Inconsistency Corrections**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 190,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ep-znM0VFcXR",
        "outputId": "5aef3519-4f46-44f6-fb17-9c1af7a7b626"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Gender : ['Male' 'Female']\n",
            "History : ['Yes' 'No']\n",
            "Patient : ['No' 'Yes']\n",
            "TakeMedication : ['No' 'Yes ' 'Yes']\n",
            "Severity : ['Mild' 'Sever' 'Moderate']\n",
            "BreathShortness : ['No' 'Yes']\n",
            "VisualChanges : ['No' 'Yes']\n",
            "NoseBleeding : ['No ' 'No' 'Yes']\n",
            "Whendiagnoused : ['<1 Year' '1 - 5 Years' '>5 Years']\n",
            "ControlledDiet : ['No' 'Yes']\n",
            "Stages : ['HYPERTENSION (Stage-1)' 'HYPERTENSION (Stage-2)' 'HYPERTENSIVE CRISIS'\n",
            " 'HYPERTENSION (Stage-2).' 'HYPERTENSIVE CRISI' 'NORMAL']\n"
          ]
        }
      ],
      "source": [
        "#checking unqiue values\n",
        "categorical_cols = [\n",
        "'Gender','History','Patient','TakeMedication','Severity',\n",
        "'BreathShortness','VisualChanges','NoseBleeding',\n",
        "'Whendiagnoused','ControlledDiet','Stages'\n",
        "]\n",
        "\n",
        "for col in categorical_cols:\n",
        "    print(col, \":\", data[col].unique())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 191,
      "metadata": {
        "id": "C8hs1ntCF6ZB"
      },
      "outputs": [],
      "source": [
        "#remove extra spaces\n",
        "for col in categorical_cols:\n",
        "    data[col] = data[col].astype(str).str.strip()\n",
        "\n",
        "#fix severity spelling\n",
        "data['Severity'] = data['Severity'].replace('Sever','Severe')\n",
        "\n",
        "#fix stage labels\n",
        "data['Stages'] = data['Stages'].replace({\n",
        "'HYPERTENSION (Stage-2).':'HYPERTENSION (Stage-2)',\n",
        "'HYPERTENSIVE CRISI':'HYPERTENSIVE CRISIS'\n",
        "})\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 192,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cqk91JX7GjKk",
        "outputId": "18f7c52f-efa8-4ec0-c74b-861731f10144"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Gender : ['Male' 'Female']\n",
            "History : ['Yes' 'No']\n",
            "Patient : ['No' 'Yes']\n",
            "TakeMedication : ['No' 'Yes']\n",
            "Severity : ['Mild' 'Severe' 'Moderate']\n",
            "BreathShortness : ['No' 'Yes']\n",
            "VisualChanges : ['No' 'Yes']\n",
            "NoseBleeding : ['No' 'Yes']\n",
            "Whendiagnoused : ['<1 Year' '1 - 5 Years' '>5 Years']\n",
            "ControlledDiet : ['No' 'Yes']\n",
            "Stages : ['HYPERTENSION (Stage-1)' 'HYPERTENSION (Stage-2)' 'HYPERTENSIVE CRISIS'\n",
            " 'NORMAL']\n"
          ]
        }
      ],
      "source": [
        "#verification\n",
        "for col in categorical_cols:\n",
        "    print(col, \":\", data[col].unique())"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LWlaXNPrIykg"
      },
      "source": [
        "**4. Duplicate Removal**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 193,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dFkgw630GknA",
        "outputId": "a8531e6c-f058-4402-8a5a-1d9beb8414b2"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(1825, 14)"
            ]
          },
          "metadata": {},
          "execution_count": 193
        }
      ],
      "source": [
        "#removing duplicates\n",
        "data.shape"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 194,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hYOXxfwUGu4O",
        "outputId": "c2f534ff-c1dd-4121-b840-1eb81e1b197c"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "np.int64(477)"
            ]
          },
          "metadata": {},
          "execution_count": 194
        }
      ],
      "source": [
        "#no. of duplicated row\n",
        "data.duplicated().sum()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 195,
      "metadata": {
        "id": "Iz6ewxONGz9Y"
      },
      "outputs": [],
      "source": [
        "#removing duplicated row\n",
        "data = data.drop_duplicates()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 196,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IDBkPTyyG7Cf",
        "outputId": "30514205-4ae0-4ed5-cbeb-c479e1ed79d6"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(1348, 14)"
            ]
          },
          "metadata": {},
          "execution_count": 196
        }
      ],
      "source": [
        "#verification\n",
        "data.shape"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3Rs07vL3J4cf"
      },
      "source": [
        "#**CATEGORIAL DATA ENCODING**\n",
        "\n",
        "---\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "onNJ-gXuNOD_"
      },
      "source": [
        "**1. Defining Features**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 197,
      "metadata": {
        "id": "dTQeabc5KQSF"
      },
      "outputs": [],
      "source": [
        "#Defining Nominal Features\n",
        "nominal_features = ['Gender','History','Patient','TakeMedication',\n",
        "'BreathShortness','VisualChanges','NoseBleeding',\n",
        "'ControlledDiet']\n",
        "\n",
        "#Defining Odinal Features\n",
        "ordinal_features = ['Age','Severity','Whendiagnoused','Systolic','Diastolic']\n",
        "\n",
        "#Defining Target Featue\n",
        "target_feature = ['Stages']\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2UUUsDvZNKYz"
      },
      "source": [
        "**2. Encoding Features**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 198,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qI5PDBoPNJWZ",
        "outputId": "6995650d-b64e-48d9-b034-bd911aacdf08"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/tmp/ipykernel_1218/1288717862.py:13: FutureWarning: Downcasting behavior in `replace` is deprecated and will be removed in a future version. To retain the old behavior, explicitly call `result.infer_objects(copy=False)`. To opt-in to the future behavior, set `pd.set_option('future.no_silent_downcasting', True)`\n",
            "  data['Severity'] = data['Severity'].replace({'Mild':0,'Moderate':1,'Severe':2})\n"
          ]
        }
      ],
      "source": [
        "#Encoding Binary Features\n",
        "for col in nominal_features:\n",
        "    if set(data[col].unique()) == set(['Yes','No']):\n",
        "        data[col] = data[col].map({'No':0,'Yes':1})\n",
        "\n",
        "#Encoding Genders\n",
        "data['Gender'] = data['Gender'].map({'Male':0,'Female':1})\n",
        "\n",
        "#Encoding Age Groups\n",
        "data['Age'] = data['Age'].map({'18-34':1,'35-50':2,'51-64':3,'65+':4})\n",
        "\n",
        "#Encoding Severity\n",
        "data['Severity'] = data['Severity'].replace({'Mild':0,'Moderate':1,'Severe':2})\n",
        "\n",
        "#Encoding Diagnosis Time\n",
        "data['Whendiagnoused'] = data['Whendiagnoused'].map({'<1 Year':1,'1 - 5 Years':2,'>5 Years':3})\n",
        "\n",
        "#Encoding Blood Pressure\n",
        "data['Systolic'] = data['Systolic'].map({'100 - 110':0,'111 - 120':1,'121 - 130':2,'130+':3})\n",
        "\n",
        "data['Diastolic'] = data['Diastolic'].map({'70 - 80':0,'81 - 90':1,'91 - 100':2,'100+':3})\n",
        "\n",
        "#Encoding Target Variable\n",
        "data['Stages'] = data['Stages'].map({'NORMAL':0,'HYPERTENSION (Stage-1)':1,'HYPERTENSION (Stage-2)':2,'HYPERTENSIVE CRISIS':3})\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "elqZLvmoNec9"
      },
      "source": [
        "**3. Aplying and Verfying**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 199,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 523
        },
        "id": "dCJOStVbNamq",
        "outputId": "7ec4558f-bd47-4ac8-8bd0-14275e295768"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Gender               int64\n",
              "Age                float64\n",
              "History              int64\n",
              "Patient              int64\n",
              "TakeMedication       int64\n",
              "Severity           float64\n",
              "BreathShortness      int64\n",
              "VisualChanges        int64\n",
              "NoseBleeding         int64\n",
              "Whendiagnoused     float64\n",
              "Systolic           float64\n",
              "Diastolic          float64\n",
              "ControlledDiet       int64\n",
              "Stages               int64\n",
              "dtype: object"
            ],
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
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Gender</th>\n",
              "      <td>int64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Age</th>\n",
              "      <td>float64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>History</th>\n",
              "      <td>int64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Patient</th>\n",
              "      <td>int64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>TakeMedication</th>\n",
              "      <td>int64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Severity</th>\n",
              "      <td>float64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>BreathShortness</th>\n",
              "      <td>int64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>VisualChanges</th>\n",
              "      <td>int64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>NoseBleeding</th>\n",
              "      <td>int64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Whendiagnoused</th>\n",
              "      <td>float64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Systolic</th>\n",
              "      <td>float64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Diastolic</th>\n",
              "      <td>float64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>ControlledDiet</th>\n",
              "      <td>int64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Stages</th>\n",
              "      <td>int64</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> object</label>"
            ]
          },
          "metadata": {},
          "execution_count": 199
        }
      ],
      "source": [
        "#Applying Feature Scaling\n",
        "from sklearn.preprocessing import MinMaxScaler\n",
        "\n",
        "scaler = MinMaxScaler()\n",
        "ordinal_features = ['Age','Severity','Whendiagnoused','Systolic','Diastolic']\n",
        "\n",
        "data[ordinal_features] = scaler.fit_transform(data[ordinal_features])\n",
        "\n",
        "#Verification\n",
        "data.head()\n",
        "data.dtypes"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Exploratory Data Analysis**\n",
        "\n",
        "---\n",
        "\n"
      ],
      "metadata": {
        "id": "Q2vjofh8P3ej"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**1. Gender Distribution**"
      ],
      "metadata": {
        "id": "D1WvaU_YRbHl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(8,4))\n",
        "sns.countplot(data=data, x=\"Gender\", palette=\"Set2\")\n",
        "plt.title(\"Gender Distribution\")\n",
        "plt.show()\n",
        "\n",
        "# Pie chart\n",
        "data['Gender'].value_counts().plot.pie(\n",
        "    autopct='%1.1f%%',\n",
        "    figsize=(5,5),\n",
        "    colors=['#66b3ff', '#99ff99']\n",
        ")\n",
        "\n",
        "plt.title(\"Gender Distribution (Pie Chart)\")\n",
        "plt.ylabel(\"\")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 800
        },
        "id": "jwex7xa7P81N",
        "outputId": "9e52c1f8-f945-4d1b-e378-ca500916ceba"
      },
      "execution_count": 200,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/tmp/ipykernel_1218/2672170775.py:2: FutureWarning: \n",
            "\n",
            "Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.\n",
            "\n",
            "  sns.countplot(data=data, x=\"Gender\", palette=\"Set2\")\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x400 with 1 Axes>"
            ],
            "image/png": "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4eHh5pGVlSVJOnnypN555x2NHj1a5eXl+vLLL/Xll1/qq6++UlJSkg4dOqQvvvjC41qTJk2SzWYzzwcOHKiamhp99tlnkr5dAayurtaUKVM8xk2dOrVeXatXr9bAgQN1ySWXmHN/+eWXSkxMVE1Njd577z2P8aNGjVJ4eHjj3qDvqXufysvLzzsmNDRU27dv17Fjxxo9T0pKioKCgho01s/PT7/73e/M84CAAP3ud79TcXGx8vPzG13Djzl+/Lh2796t8ePHe6yGX3nllbrpppv01ltv1XvNvffe63E+cOBAffXVV+bfQwAXF7YlAGh12rZtK0mqqKio1/fcc8+pvLxcRUVFHh+wOnz4sAzD0MMPP6yHH374nNctLi5Whw4dzPNOnTp59F9yySWSvv1f6pLMkNu9e3ePceHh4ebYOocOHdJHH3103sBaXFzscd6lS5dzjmuMuvep7n07l4ULFyolJUWxsbHq27evhg0bpnHjxqlr164NnudCao6JiVFwcLBH22WXXSbp232y/fv3b/C1LkTdn9nll19er69nz556++23VVlZ6VHbD/09cDgczVIngOZDuAXQ6jidTkVHR5/zUVJ1e3C//yGkug9tzZgxQ0lJSee8brdu3TzOz/foKKMRT0isra3VTTfdpAceeOCc/XXBrk5DV0Abou59+v79fdfo0aM1cOBArVmzRhs2bNATTzyhBQsW6NVXX9XQoUMbNE9T1izJYzX8u2pqapp0nh/TlH8PAHgf4RZAq5ScnKy//vWv2rFjh375y1/+6Pi6FUh/f38lJiY2SQ11z889dOiQxwrniRMnzNXdOpdeeqkqKiqabO6Gqqio0Jo1axQbG6uePXv+4Njo6Gjdd999uu+++1RcXKyrr75ajz/+uBluzxc2G+PYsWP1Vkg/+eQTSTI/0FW3QlpSUuLx2rrV1+9qaG11f2YHDx6s13fgwAG1b9++3ooyAGthzy2AVumBBx5QmzZtdM8996ioqKhe//dX1SIiIjRo0CA999xzOn78eL3x33/EV0MkJibK399fzzzzjMd85/qmrNGjRysvL09vv/12vb6SkhKdPXv2guf/Md98843Gjh2rkydP6qGHHvrBldDS0lKPtoiICMXExKiqqspsCw4Orjeusc6ePavnnnvOPK+urtZzzz2n8PBw9e3bV9K3/0EgyWM/ck1NjZ5//vl612tobdHR0erTp49eeOEFj9C8d+9ebdiwQcOGDWvsLQG4SLByC6BV6t69u1auXKm77rpLl19+ufkNZYZhqKCgQCtXrpSPj486duxoviYrK0vXXXedevXqpYkTJ6pr164qKipSXl6ePv/8c3344YcXVEN4eLhmzJihzMxMDR8+XMOGDdO///1vrVu3Tu3bt/cYO3PmTL3++usaPny4xo8fr759+6qyslJ79uzRK6+8ok8//bTeay7EF198oRdffFHSt6u1+/fvN7+hbPr06R4f3vq+8vJydezYUbfffrt69+6tkJAQbdq0STt37tRTTz1ljuvbt69efvllpaen65prrlFISIhGjBjRqHpjYmK0YMECffrpp7rsssv08ssva/fu3Xr++efl7+8vSbriiivUv39/ZWRk6OTJkwoLC9OqVavO+R8CF1LbE088oaFDh8rlcmnChAnmo8CcTqfHs38BWJQ3H9UAAD/m8OHDRmpqqtGtWzcjMDDQCAoKMnr06GHce++9xu7du+uNP3LkiDFu3DgjKirK8Pf3Nzp06GAMHz7ceOWVV8wxdY+g2rlzp8drz/UIqpqaGuORRx4xoqOjjaCgIGPQoEHG3r17jbi4OI9HgRmGYZSXlxsZGRlGt27djICAAKN9+/bGtddeazz55JPm46/qHl31xBNPNPg9iIuLMyQZkgybzWY4HA7jiiuuMCZOnGhs3779nK/Rdx4FVlVVZcycOdPo3bu30bZtWyM4ONjo3bu3sWTJEo/XVFRUGL/5zW+M0NBQQ5L56K2692X16tX15jnfo8CuuOIK44MPPjBcLpcRGBhoxMXFGc8++2y91x85csRITEw07Ha7ERkZafzxj380Nm7cWO+a56vtXI8CMwzD2LRpkzFgwAAjKCjIcDgcxogRI4z9+/d7jKl7FNiJEyc82s/3iDIAFwebYbBjHgAAANbAnlsAAABYBuEWAAAAlkG4BQAAgGUQbgEAAGAZhFsAAABYBuEWAAAAluHVL3Ho3LnzOb9m8b777lNWVpZOnz6t6dOna9WqVaqqqlJSUpKWLFmiyMhIc2xhYaFSU1P17rvvKiQkRCkpKcrMzJSfX8Nvrba2VseOHVPbtm2b9OsnAQAA0DQMw1B5ebliYmLk43P+9VmvhtudO3eqpqbGPN+7d69uuukm3XHHHZKkadOm6c0339Tq1avldDo1efJk3XbbbXr//fclffs1jcnJyYqKitLWrVt1/PhxjRs3Tv7+/po/f36D6zh27JhiY2Ob9uYAAADQ5I4ePerx7ZTf16q+xGHq1KnKycnRoUOHVFZWpvDwcK1cuVK33367JOnAgQPq2bOn8vLy1L9/f61bt07Dhw/XsWPHzNXcZcuW6cEHH9SJEycUEBDQoHlLS0sVGhqqo0ePyuFwNNv9AQAAoHHKysoUGxurkpISOZ3O847z6srtd1VXV+vFF19Uenq6bDab8vPzdebMGSUmJppjevTooU6dOpnhNi8vT7169fLYppCUlKTU1FTt27dPV1111TnnqqqqUlVVlXleXl4uSXI4HIRbAACAVuzHtpC2mg+UrV27ViUlJRo/frwkye12KyAgQKGhoR7jIiMj5Xa7zTHfDbZ1/XV955OZmSmn02kebEkAAACwhlYTbpcvX66hQ4cqJiam2efKyMhQaWmpeRw9erTZ5wQAAEDzaxXbEj777DNt2rRJr776qtkWFRWl6upqlZSUeKzeFhUVKSoqyhyzY8cOj2sVFRWZfedjt9tlt9ub8A4AAADQGrSKldvs7GxFREQoOTnZbOvbt6/8/f2Vm5trth08eFCFhYVyuVySJJfLpT179qi4uNgcs3HjRjkcDsXHx7fcDQAAAKBV8PrKbW1trbKzs5WSkuLxbFqn06kJEyYoPT1dYWFhcjgcmjJlilwul/r37y9JGjJkiOLj4zV27FgtXLhQbrdbs2bNUlpaGiuzAAAAP0NeD7ebNm1SYWGh7rnnnnp9ixYtko+Pj0aNGuXxJQ51fH19lZOTo9TUVLlcLgUHByslJUXz5s1ryVsAAABAK9GqnnPrLWVlZXI6nSotLeVRYAAAAK1QQ/Naq9hzCwAAADQFwi0AAAAsg3ALAAAAyyDcAgAAwDK8/rQESNPX/d3bJQBoJk8NHeftEryieOkD3i4BQDOJSF3o7RJ+ECu3AAAAsAzCLQAAACyDcAsAAADLINwCAADAMgi3AAAAsAzCLQAAACyDcAsAAADLINwCAADAMgi3AAAAsAzCLQAAACyDcAsAAADLINwCAADAMgi3AAAAsAzCLQAAACyDcAsAAADLINwCAADAMgi3AAAAsAzCLQAAACyDcAsAAADLINwCAADAMgi3AAAAsAzCLQAAACyDcAsAAADLINwCAADAMgi3AAAAsAzCLQAAACyDcAsAAADLINwCAADAMrwebr/44gv99re/Vbt27RQUFKRevXrpgw8+MPsNw9Ds2bMVHR2toKAgJSYm6tChQx7XOHnypMaMGSOHw6HQ0FBNmDBBFRUVLX0rAAAA8DKvhtuvv/5aAwYMkL+/v9atW6f9+/frqaee0iWXXGKOWbhwoZ5++mktW7ZM27dvV3BwsJKSknT69GlzzJgxY7Rv3z5t3LhROTk5eu+99zRp0iRv3BIAAAC8yM+bky9YsECxsbHKzs4227p06WL+bBiGFi9erFmzZumWW26RJP39739XZGSk1q5dqzvvvFMff/yx1q9fr507d6pfv36SpGeeeUbDhg3Tk08+qZiYmJa9KQAAAHiNV1duX3/9dfXr10933HGHIiIidNVVV+kvf/mL2V9QUCC3263ExESzzel0KiEhQXl5eZKkvLw8hYaGmsFWkhITE+Xj46Pt27efc96qqiqVlZV5HAAAALj4eTXc/uc//9HSpUvVvXt3vf3220pNTdX999+vF154QZLkdrslSZGRkR6vi4yMNPvcbrciIiI8+v38/BQWFmaO+b7MzEw5nU7ziI2NbepbAwAAgBd4NdzW1tbq6quv1vz583XVVVdp0qRJmjhxopYtW9as82ZkZKi0tNQ8jh492qzzAQAAoGV4NdxGR0crPj7eo61nz54qLCyUJEVFRUmSioqKPMYUFRWZfVFRUSouLvboP3v2rE6ePGmO+T673S6Hw+FxAAAA4OLn1XA7YMAAHTx40KPtk08+UVxcnKRvP1wWFRWl3Nxcs7+srEzbt2+Xy+WSJLlcLpWUlCg/P98c884776i2tlYJCQktcBcAAABoLbz6tIRp06bp2muv1fz58zV69Gjt2LFDzz//vJ5//nlJks1m09SpU/XYY4+pe/fu6tKlix5++GHFxMRo5MiRkr5d6b355pvN7QxnzpzR5MmTdeedd/KkBAAAgJ8Zr4bba665RmvWrFFGRobmzZunLl26aPHixRozZow55oEHHlBlZaUmTZqkkpISXXfddVq/fr0CAwPNMS+99JImT56sG2+8UT4+Pho1apSefvppb9wSAAAAvMhmGIbh7SK8raysTE6nU6WlpV7Zfzt93d9bfE4ALeOpoeO8XYJXFC99wNslAGgmEakLvTJvQ/Oa179+FwAAAGgqhFsAAABYBuEWAAAA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s3HjRjkcDsXHx7d47QAAAPAur67cZmRkaOjQoerUqZPKy8u1cuVKbd68WW+//bacTqcmTJig9PR0hYWFyeFwaMqUKXK5XOrfv78kaciQIYqPj9fYsWO1cOFCud1uzZo1S2lpaazMAgAA/Ax5NdwWFxdr3LhxOn78uJxOp6688kq9/fbbuummmyRJixYtko+Pj0aNGqWqqiolJSVpyZIl5ut9fX2Vk5Oj1NRUuVwuBQcHKyUlRfPmzfPWLQEAAMCLvBpuly9f/oP9gYGBysrKUlZW1nnHxMXF6a233mrq0gAAAHARanV7bgEAAIDGItwCAADAMgi3AAAAsAzCLQAAACyDcAsAAADLINwCAADAMgi3AAAAsAzCLQAAACyDcAsAAADLINwCAADAMgi3AAAAsAzCLQAAACyDcAsAAADLINwCAADAMgi3AAAAsAzCLQAAACyDcAsAAADLINwCAADAMgi3AAAAsAzCLQAAACyDcAsAAADLINwCAADAMgi3AAAAsAzCLQAAACyDcAsAAADLINwCAADAMgi3AAAAsAzCLQAAACyDcAsAAADLINwCAADAMgi3AAAAsAzCLQAAACyDcAsAAADL8Gq4zczM1DXXXKO2bdsqIiJCI0eO1MGDBz3GnD59WmlpaWrXrp1CQkI0atQoFRUVeYwpLCxUcnKy2rRpo4iICM2cOVNnz55tyVsBAABAK+DVcLtlyxalpaVp27Zt2rhxo86cOaMhQ4aosrLSHDNt2jS98cYbWr16tbZs2aJjx47ptttuM/tramqUnJys6upqbd26VS+88IJWrFih2bNne+OWAAAA4EV+3px8/fr1HucrVqxQRESE8vPzdf3116u0tFTLly/XypUrNXjwYElSdna2evbsqW3btql///7asGGD9u/fr02bNikyMlJ9+vTRo48+qgcffFBz585VQECAN24NAAAAXtCq9tyWlpZKksLCwiRJ+fn5OnPmjBITE80xPXr0UKdOnZSXlydJysvLU69evRQZGWmOSUpKUllZmfbt23fOeaqqqlRWVuZxAAAA4OLXasJtbW2tpk6dqgEDBugXv/iFJMntdisgIEChoaEeYyMjI+V2u80x3w22df11feeSmZkpp9NpHrGxsU18NwAAAPCGVhNu09LStHfvXq1atarZ58rIyFBpaal5HD16tNnnBAAAQPPz6p7bOpMnT1ZOTo7ee+89dezY0WyPiopSdXW1SkpKPFZvi4qKFBUVZY7ZsWOHx/XqnqZQN+b77Ha77HZ7E98FAAAAvM2rK7eGYWjy5Mlas2aN3nnnHXXp0sWjv2/fvvL391dubq7ZdvDgQRUWFsrlckmSXC6X9uzZo+LiYnPMxo0b5XA4FB8f3zI3AgAAgFbBqyu3aWlpWrlypV577TW1bdvW3CPrdDoVFBQkp9OpCRMmKD09XWFhYXI4HJoyZYpcLpf69+8vSRoyZIji4+M1duxYLVy4UG63W7NmzVJaWhqrswAAAD8zXg23S5culSQNGjTIoz07O1vjx4+XJC1atEg+Pj4aNWqUqqqqlJSUpCVLlphjfX19lZOTo9TUVLlcLgUHByslJUXz5s1rqdsAAABAK+HVcGsYxo+OCQwMVFZWlrKyss47Ji4uTm+99VZTlgYAAICLUKt5WgIAAADwUxFuAQAAYBmEWwAAAFgG4RYAAACWQbgFAACAZRBuAQAAYBmEWwAAAFgG4RYAAACWQbgFAACAZRBuAQAAYBmEWwAAAFgG4RYAAACWQbgFAACAZRBuAQAAYBmEWwAAAFgG4RYAAACWQbgFAACAZRBuAQAAYBmEWwAAAFgG4RYAAACWQbgFAACAZRBuAQAAYBmEWwAAAFgG4RYAAACWQbgFAACAZRBuAQAAYBmEWwAAAFgG4RYAAACWQbgFAACAZRBuAQAAYBmEWwAAAFgG4RYAAACW4dVw+95772nEiBGKiYmRzWbT2rVrPfoNw9Ds2bMVHR2toKAgJSYm6tChQx5jTp48qTFjxsjhcCg0NFQTJkxQRUVFC94FAAAAWguvhtvKykr17t1bWVlZ5+xfuHChnn76aS1btkzbt29XcHCwkpKSdPr0aXPMmDFjtG/fPm3cuFE5OTl67733NGnSpJa6BQAAALQift6cfOjQoRo6dOg5+wzD0OLFizVr1izdcsstkqS///3vioyM1Nq1a3XnnXfq448/1vr167Vz507169dPkvTMM89o2LBhevLJJxUTE9Ni9wIAAADva7V7bgsKCuR2u5WYmGi2OZ1OJSQkKC8vT5KUl5en0NBQM9hKUmJionx8fLR9+/bzXruqqkplZWUeBwAAAC5+rTbcut1uSVJkZKRHe2RkpNnndrsVERHh0e/n56ewsDBzzLlkZmbK6XSaR2xsbBNXDwAAAG9oteG2OWVkZKi0tNQ8jh496u2SAAAA0ARabbiNioqSJBUVFXm0FxUVmX1RUVEqLi726D979qxOnjxpjjkXu90uh8PhcQAAAODi12rDbZcuXRQVFaXc3FyzraysTNu3b5fL5ZIkuVwulZSUKD8/3xzzzjvvqLa2VgkJCS1eMwAAALzLq09LqKio0OHDh83zgoIC7d69W2FhYerUqZOmTp2qxx57TN27d1eXLl308MMPKyYmRiNHjpQk9ezZUzfffLMmTpyoZcuW6cyZM5o8ebLuvPNOnpQAAADwM+TVcPvBBx/oV7/6lXmenp4uSUpJSdGKFSv0wAMPqLKyUpMmTVJJSYmuu+46rV+/XoGBgeZrXnrpJU2ePFk33nijfHx8NGrUKD399NMtfi8AAADwPq+G20GDBskwjPP222w2zZs3T/PmzTvvmLCwMK1cubI5ygMAAMBFptXuuQUAAAAuFOEWAAAAlkG4BQAAgGUQbgEAAGAZhFsAAABYBuEWAAAAlkG4BQAAgGUQbgEAAGAZhFsAAABYBuEWAAAAlkG4BQAAgGUQbgEAAGAZhFsAAABYBuEWAAAAlkG4BQAAgGUQbgEAAGAZhFsAAABYBuEWAAAAlkG4BQAAgGUQbgEAAGAZhFsAAABYBuEWAAAAlkG4BQAAgGUQbgEAAGAZhFsAAABYBuEWAAAAlkG4BQAAgGUQbgEAAGAZhFsAAABYBuEWAAAAlkG4BQAAgGUQbgEAAGAZhFsAAABYhmXCbVZWljp37qzAwEAlJCRox44d3i4JAAAALcwS4fbll19Wenq65syZo127dql3795KSkpScXGxt0sDAABAC7JEuP3zn/+siRMn6u6771Z8fLyWLVumNm3a6G9/+5u3SwMAAEAL8vN2AT9VdXW18vPzlZGRYbb5+PgoMTFReXl553xNVVWVqqqqzPPS0lJJUllZWfMWex5Vp77xyrwAmp+3fq94W/k3VT8+CMBFKdBLv9fqfp8ahvGD4y76cPvll1+qpqZGkZGRHu2RkZE6cODAOV+TmZmpRx55pF57bGxss9QI4OcrS/d6uwQAaFrTn/bq9OXl5XI6neftv+jDbWNkZGQoPT3dPK+trdXJkyfVrl072Ww2L1YGqysrK1NsbKyOHj0qh8Ph7XIA4Cfj9xpaimEYKi8vV0xMzA+Ou+jDbfv27eXr66uioiKP9qKiIkVFRZ3zNXa7XXa73aMtNDS0uUoE6nE4HPwjAMBS+L2GlvBDK7Z1LvoPlAUEBKhv377Kzc0122pra5WbmyuXy+XFygAAANDSLvqVW0lKT09XSkqK+vXrp1/+8pdavHixKisrdffdd3u7NAAAALQgS4TbX//61zpx4oRmz54tt9utPn36aP369fU+ZAZ4m91u15w5c+ptiwGAixW/19Da2Iwfe54CAAAAcJG46PfcAgAAAHUItwAAALAMwi0AAAAsg3ALAAAAyyDcAi0kKytLnTt3VmBgoBISErRjxw5vlwQAjfbee+9pxIgRiomJkc1m09q1a71dEiCJcAu0iJdfflnp6emaM2eOdu3apd69eyspKUnFxcXeLg0AGqWyslK9e/dWVlaWt0sBPPAoMKAFJCQk6JprrtGzzz4r6dtv0YuNjdWUKVP0hz/8wcvVAcBPY7PZtGbNGo0cOdLbpQCs3ALNrbq6Wvn5+UpMTDTbfHx8lJiYqLy8PC9WBgCA9RBugWb25Zdfqqampt435kVGRsrtdnupKgAArIlwCwAAAMsg3ALNrH379vL19VVRUZFHe1FRkaKiorxUFQAA1kS4BZpZQECA+vbtq9zcXLOttrZWubm5crlcXqwMAADr8fN2AcDPQXp6ulJSUtSvXz/98pe/1OLFi1VZWam7777b26UBQKNUVFTo8OHD5nlBQYF2796tsLAwderUyYuV4eeOR4EBLeTZZ5/VE088IbfbrT59+ujpp59WQkKCt8sCgEbZvHmzfvWrX9VrT0lJ0YoVK1q+IOD/R7gFAACAZbDnFgAAAJZBuAUAAIBlEG4BAABgGYRbAAAAWAbhFgAAAJZBuAUAAIBlEG4BAABgGYRbAAAAWAbhFgB+pgYNGqSpU6d6uwwAaFKEWwDwIrfbrd///vfq1q2bAgMDFRkZqQEDBmjp0qU6deqUt8sDgIuOn7cLAICfq//85z8aMGCAQkNDNX/+fPXq1Ut2u1179uzR888/rw4dOui//uu/vF3medXU1Mhms8nHh3USAK0Hv5EAwEvuu+8++fn56YMPPtDo0aPVs2dPde3aVbfccovefPNNjRgxQpJUUlKi//f//p/Cw8PlcDg0ePBgffjhh+Z15s6dqz59+ugf//iHOnfuLKfTqTvvvFPl5eXmmMrKSo0bN04hISGKjo7WU089Va+eqqoqzZgxQx06dFBwcLASEhK0efNms3/FihUKDQ3V66+/rvj4eNntdhUWFjbfGwQAjUC4BQAv+Oqrr7RhwwalpaUpODj4nGNsNpsk6Y477lBxcbHWrVun/Px8XX311brxxht18uRJc+yRI0e0du1a5eTkKCcnR1u2bNGf/vQns3/mzJnasmWLXnvtNW3YsEGbN2/Wrl27POabPHmy8vLytGrVKn300Ue64447dPPNN+vQoUPmmFOnTmnBggX661//qn379ikiIqIp3xYA+MnYlgAAXnD48GEZhqHLL7/co719+/Y6ffq0JCktLU0jRozQjh07VFxcLLvdLkl68skntXbtWr3yyiuaNGmSJKm2tlYrVqxQ27ZtJUljx45Vbm6uHn/8cVVUVGj58uV68cUXdeONN0qSXnjhBXXs2NGct7CwUNnZ2SosLFRMTIwkacaMGVq/fr2ys7M1f/58SdKZM2e0ZMkS9e7duxnfHQBoPMItALQiO3bsUG1trcaMGaOqqip9+OGHqqioULt27TzGffPNNzpy5Ih53rlzZzPYSlJ0dLSKi4slfbuqW11drYSEBLM/LCzMI1jv2bNHNTU1uuyyyzzmqaqq8pg7ICBAV155ZdPcLAA0A8ItAHhBt27dZLPZdPDgQY/2rl27SpKCgoIkSRUVFYqOjvbY+1onNDTU/Nnf39+jz2azqba2tsH1VFRUyNfXV/n5+fL19fXoCwkJMX8OCgoyt0sAQGtEuAUAL2jXrp1uuukmPfvss5oyZcp5991effXVcrvd8vPzU+fOnRs116WXXip/f39t375dnTp1kiR9/fXX+uSTT3TDDTdIkq666irV1NSouLhYAwcObNQ8ANAa8IEyAPCSJUuW6OzZs+rXr59efvllffzxxzp48KBefPFFHThwQL6+vkpMTJTL5dLIkSO1YcMGffrpp9q6daseeughffDBBw2aJyQkRBMmTNDMmTP1zjvvaO/evRo/frzHI7wuu+wyjRkzRuPGjdOrr76qgoIC7dixQ5mZmXrzzTeb6y0AgCbHyi0AeMmll16qf//735o/f74yMjL0+eefy263Kz4+XjNmzNB9990nm82mt956Sw899JDuvvtunThxQlFRUbr++usVGRnZ4LmeeOIJVVRUaMSIEWrbtq2mT5+u0tJSjzHZ2dl67LHHNH36dH3xxRdq3769+vfvr+HDhzf1rQNAs7EZhmF4uwgAAACgKbAtAQAAAJZBuAUAAIBlEG4BAABgGYRbAAAAWAbhFgAAAJZBuAUAAIBlEG4BAABgGYRbAAAAWAbhFgAAAJZBuAUAAIBlEG4BAABgGf8fQfK5DPXKsUsAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 500x500 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAZQAAAGrCAYAAADn6WHYAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAANftJREFUeJzt3Xd8VHW+//HXpBdSCAklAQKhh6qAisDK7kZ5ABZc/WHbC+oKCpZdy7q6ru26Xi+yey3YG7rs6ioqdldFwRVBVDrSMQGpKSSkkJD2/f0xZJaQQhJOcuaceT958ICcmTPzmczM932+3+8pHmOMQURE5CQF2V2AiIi4gwJFREQsoUARERFLKFBERMQSChQREbGEAkVERCyhQBEREUsoUERExBIKFBERsYQCxUV69OjBlVdeaXcZDfJ4PNx3332t/jxLlizB4/GwZMkS37Jx48YxaNCgVn9ugKysLDweDy+//HKbPF99Jk6cyPTp05u93n333YfH42mFiprG4/Fwww032Pb8ABUVFXTr1o2nnnrK1jqcSIHSApmZmdxwww307duXqKgooqKiSE9P5/rrr2fdunV2l9cmevTogcfjwePxEBQURHx8PIMHD2bGjBmsWLHCsud59dVXefTRRy17PCv5a21ff/01n376KX/4wx98y2pCtuZvaGgoaWlpTJ06lR9//LHVa9qxYwfXXnstaWlpREREEBsby+jRo3nssccoLS1t9eevz7Jly7jvvvsoKCiotTw0NJRbbrmFBx98kLKyMltqcywjzfL++++bqKgoExsba2bOnGmeeeYZ89xzz5lbbrnF9OjRw3g8HpOVlWVLbampqWbatGlt9lzDhg0z8+fPN/PnzzdPPfWUufHGG03nzp0NYG6++eY665SWlpqKiopmPc+kSZNMampqs9apqqoypaWlpqqqyrfsrLPOMgMHDmzW47S0turqalNaWmoqKystfb6muuCCC8w555xTa9nixYsNYG666SYzf/5889JLL5kbbrjBhIWFmYSEBLNnzx5jjDEVFRWmtLTU0no++OADExkZaeLj481NN91knnvuOfPEE0+YSy+91ISGhprp06f77guY66+/3tLnb8icOXMMYDIzM+vclp+fb8LCwsyLL77YJrW4RYi9ceYsO3bs4NJLLyU1NZXPP/+cLl261Lp99uzZPPXUUwQFOb/jV1lZSXV1NWFhYQ3eJyUlhV//+te1ls2ePZvLL7+cRx55hD59+jBz5kzfbREREa1WL0BZWRlhYWEEBQW1+nM1xuPx2Pb82dnZfPjhhzzzzDP13j527FguvvhiAK666ir69u3LTTfdxCuvvMKdd95JSEgIISHWNQuZmZm+78wXX3xR6ztz/fXXs337dj788EPLnq8pSkpKiI6ObvQ+8fHxnHPOObz88stcffXVbVSZC9idaE4yY8YMA5hvvvmmWett2rTJXHTRRaZ9+/YmPDzcDB8+3Lz77ru17jNv3jwDmKVLl5qbb77ZJCYmmqioKDN58mSTnZ1d677V1dXmgQceMCkpKSYyMtKMGzfObNiwod4eSn5+vvntb39runbtasLCwkyvXr3M//7v/9baes/MzDSAmTNnjnnkkUdMWlqaCQoKMqtXr27wNaWmpppJkybVe1tRUZFJSEgwKSkpprq62rccMPfee6/v58LCQvPb3/7WpKammrCwMJOUlGQyMjLMypUrjTHeXgVQ629Nj6Bmi/u1114zd911l0lOTjYej8fk5+f7blu8eLHvuWp6KN9//70ZNWqUiYiIMD169DBPP/10ve/D8Vutxz9mY7XV/D7nzZtX6zE+//xzM2bMGBMVFWXi4uLM+eefbzZu3FjrPvfee68BzLZt28y0adNMXFyciY2NNVdeeaUpKSlp8P2o8dJLLxmgTi+5pv4FCxbUWr5hwwYD+HoJNc9/vPnz55tTTz3VREREmPbt25tLLrnE7Nq164T1XHfddQYwX3/99Qnva8x/eigLFy40AwcONGFhYSY9Pd18/PHHte6XlZVlZs6cafr27WsiIiJMQkKCufjii+u8bzXv55IlS8zMmTNNUlKSiY+P973O4/8eu/5jjz1mPB6PycvLa1Ltoh5Ks3zwwQf07t2b008/vcnr/PDDD4wePZqUlBTuuOMOoqOjeeONN5g8eTJvvfUWF154Ya3733jjjbRv3557772XrKwsHn30UW644QZef/11333uuece/vznPzNx4kQmTpzIqlWrOOeccygvL6/1WIcPH+ass85iz549XHvttXTv3p1ly5Zx5513sm/fvjrj//PmzaOsrIwZM2YQHh5OQkJC839JQLt27bjwwgt58cUX2bhxIwMHDqz3ftdddx1vvvkmN9xwA+np6eTl5bF06VI2bdrEqaee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AU74GZb/0BxKM9x+++1ERUVx9dVXc+DAgTq3H7/12LFjR8aNG8ezzz7Lvn376tw/Jyen2TVkZGQQGhrK3Llzaz1ffUdsT5kyheXLl/PJJ5/Uua2goIDKyspmP/+JlJaW8l//9V8cPHiQu+66q9Et/uOHJjp27EhycjJHjhzxLYuOjq53CKMlKisrefbZZ30/l5eX8+yzz5KUlMTw4cMBfGP3x84vVVVV8dxzz9V5vKbW1qVLF4YNG8Yrr7xSq8HbsGEDn376KRMnTmzpS6pj1KhR5OfnW3b0+69+9SuCg4O5//7763y+jTHk5eU1uv7tt99OdHQ011xzTb3fmR07dvDYY481u67g4OA69cydO7dZPcmaEG8ohFauXInH47E0CN1OPZRm6NOnD6+++iqXXXYZ/fr144orrmDo0KEYY8jMzOTVV18lKCiIrl27+tZ58sknGTNmDIMHD2b69OmkpaVx4MABli9fzu7du1m7dm2zakhKSuK2227joYce4txzz2XixImsXr2ajz/+uE7X/Pe//z3vvfce5557LldeeSXDhw+npKSE9evX8+abb5KVlXVS3fk9e/bw97//HfD2SjZu3MiCBQvYv38/t956a60J8OMVFRXRtWtXLr74YoYOHUq7du1YtGgR3333Xa2tzuHDh/P6669zyy23MHLkSNq1a8d5553XonqTk5OZPXs2WVlZ9O3bl9dff501a9bw3HPP+eYCBg4cyBlnnMGdd97JwYMHSUhI4J///Ge94duc2ubMmcOECRMYNWoUv/nNb3y7DcfFxVl6frNJkyYREhLCokWLmDFjxkk/Xq9evfjzn//MnXfeSVZWFpMnTyYmJobMzEwWLlzIjBkzuO222xpd/9VXX+WSSy5hwIABTJ06lUGDBlFeXs6yZctYsGBBi84/d+655zJ//nzi4uJIT09n+fLlLFq0qNHdn49XsxFx1113cemllxIaGsp5553nC5rPPvuM0aNHN+sxA54Ne5Y53vbt283MmTNN7969TUREhImMjDT9+/c31113nVmzZk2d++/YscNMnTrVdO7c2YSGhpqUlBRz7rnnmjfffNN3n5rdG2t236xR3+6qVVVV5v777zddunQ54YGNRUVF5s477zS9e/c2YWFhJjEx0Zx55pnmL3/5i29X2WMPbGyq1NRU38FgHo/HxMbGmoEDB5rp06ebFStW1LsOx+w2fOTIEfP73//eDB061MTExJjo6GgzdOhQ89RTT9Vap7i42Fx++eUmPj6+3gMbjz9Qr6HfWX0HNqampponnniizvo7duwwGRkZJjw83HTq1Mn88Y9/NJ999lmdx2yotoYObFy0aJEZPXq0iYyMNLGxsea8885r8MDGnJycWssb2p25Pueff7755S9/We/vpL7fV33Pf7y33nrLjBkzxkRHR5vo6GjTv39/c/3115stW7acsB5jjNm6dauZPn266dGjhwkLCzMxMTFm9OjRZu7cubV2qaeBU68c/9nOz883V111lUlMTDTt2rUz48ePN5s3b65zv4a+VzVqDhAOCgqq9fstKCgwYWFh5oUXXmjS6xMvjzEtmO0VEb/11VdfMW7cODZv3tzg3lnSuEcffZSHH36YHTt2WL7jh5spUERcaMKECXTt2pXnn3/e7lIcp6Kigl69enHHHXcwa9Ysu8txFAWKiIhYQnt5iYiIJRQoIiJiCQWKiIhYQoEiIiKWUKCIiIglFCgiImIJBYqIiFhCgSIiIpZQoIiIiCUUKCIiYgkFioiIWEKBIiIillCgiIiIJRQoIiJiCQWKiIhYQoEiIiKWUKCIiIglFCgiImIJBYqIiFhCgSIiIpZQoIiIiCUUKCIiYgkFishxnnzySXr06EFERASnn3463377rd0liTiCAkXkGK+//jq33HIL9957L6tWrWLo0KGMHz+e7Oxsu0sT8XseY4yxuwgRf3H66aczcuRInnjiCQCqq6vp1q0bN954I3fccYfN1Yn4N/VQRI4qLy9n5cqVZGRk+JYFBQWRkZHB8uXLbaxMxBkUKCJH5ebmUlVVRadOnWot79SpE/v377epKhHnUKCIiIglFCgiRyUmJhIcHMyBAwdqLT9w4ACdO3e2qSoR51CgiBwVFhbG8OHD+fzzz33Lqqur+fzzzxk1apSNlYk4Q4jdBYj4k1tuuYVp06YxYsQITjvtNB599FFKSkq46qqr7C5NxO8pUESOcckll5CTk8M999zD/v37GTZsGP/617/qTNSLSF06DkVERCyhORQREbGEAkVERCyhQBEREUsoUERExBIKFBERsYQCRURELKFAERERSyhQRETEEgoUERGxhAJFREQsoXN5SUCqqILiciirPPq3Co4c/f+Roz9XVYMBjPH+6wE8Hu+/wUEQEQzh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XKecckpO8KeMslavI4IIok/wR3tfiZsoUCQgVVJJGWVUUkk55VTU86eaat+QmsH4jiT34CGIIELr+RNGGCGEEEGEehkScBQoIiJiCe2oLiIillCgiIiIJRQoIiJiCQWKiIhYQoEiIiKWUKCIiIglFCgiImIJBYqIiFhCgSLSDP/+978577zzSE5OxuPx8M4779hdkojfUKCINENJSQlDhw7lySeftLsUEb+jkw2JNMOECROYMGGC3WWI+CX1UERExBIKFBERsYQCRURELKFAERERSyhQRETEEtrLS6QZiouL2b59u+/nzMxM1qxZQ0JCAt27d7exMhH76YqNIs2wZMkSfv7zn9dZPm3aNF5++eW2L0jEjyhQRETEEppDERERSyhQRETEEgoUERGxhAJFREQsoUARERFLKFBERMQSChQREbGEAkVERCyhQBEREUsoUERExBIKFBERsYQCRURELKFAERERSyhQRETEEgoUERGxhAJFREQsoUARERFLKFBERMQSChQREbGEAkVERCyhQBEREUsoUERExBIKFBERsYQCRURELKFAERERSyhQRETEEgoUERGxhAJFREQs8f8B1czWCKOGfeQAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**2. Hypertension Stages Distribution**"
      ],
      "metadata": {
        "id": "O6hxGRDORffB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(8,4))\n",
        "\n",
        "sns.countplot(data=data, x=\"Stages\", palette=\"coolwarm\")\n",
        "\n",
        "plt.title(\"Hypertension Stages Distribution\")\n",
        "\n",
        "plt.xticks(rotation=30)\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 375
        },
        "id": "qvGOYF7JQcDj",
        "outputId": "4a0e6161-2c2d-4af3-82c7-1f5121308bdc"
      },
      "execution_count": 201,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/tmp/ipykernel_1218/3132479274.py:3: FutureWarning: \n",
            "\n",
            "Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.\n",
            "\n",
            "  sns.countplot(data=data, x=\"Stages\", palette=\"coolwarm\")\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x400 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAArcAAAGMCAYAAADAyIqEAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAPjdJREFUeJzt3XlclFX///E3OwgCojC44W6ISypuZKkpiUqaSZlmSt2md4rlUmZUmmumldriUj1S6zazzFtvs9xyqxQVTc19S8PSATdANAHh+v3Rj/k2IYmojFy+no/HPB7NOWeu63ONl/bmcOaMk2EYhgAAAAATcHZ0AQAAAMDNQrgFAACAaRBuAQAAYBqEWwAAAJgG4RYAAACmQbgFAACAaRBuAQAAYBqEWwAAAJgG4RYAAACmQbgFgL+YO3eunJycdPz4cUeXggIcP35cTk5Omjt37i0/19Xuh6pVq+rBBx+85eeWpPXr18vJyUnr168vlvMBZkC4BUqovP/pbtu27ar9bdq0Ub169Yq5quu3adMmjR49WqmpqY4uxeGysrL0zjvvqFGjRvL19ZW/v7/q1q2r/v3768CBA7ZxZnvPnJycbA9XV1cFBAQoPDxcgwcP1r59+27aeWbMmFEsgbgobufagJLGyTAMw9FFALh+c+fO1VNPPaXExEQ1adIkX3+bNm105swZ7dmzxwHVFd5bb72l4cOH69ixY6pataqjy1FOTo6ys7Pl4eEhJyenYj13586dtXz5cvXs2VMRERHKzs7WgQMHtGzZMo0bN05PPvmkpNvvPbtRTk5OeuCBB9SnTx8ZhqG0tDTt2rVLCxcu1MWLFzVp0iQNGzbMNt4wDGVmZsrNzU0uLi6FPk+9evVUrly565oFvdr9ULVqVdWrV0/Lli0r9HGKWltubq6ysrLk7u4uZ2fmo4DCcHV0AQDuTBcvXpS3t7ejy8jHxcXlugLTzZKYmKhly5ZpwoQJevnll+363n//fdPM0hakdu3aeuKJJ+za3njjDXXu3FnPP/+8QkND1alTJ0l/hmFPT89bWk/e/emo+yGPs7PzLb9WwGz4MRC4Q7Ru3Vp33333VfvuuusuRUVFSfq/9YxvvfWWpk6dqipVqsjLy0utW7e+6izwgQMH9MgjjyggIECenp5q0qSJli5dajcmbwnFhg0bNHDgQAUFBalSpUoaPXq0hg8fLkmqVq2a7VfTf13fOG/ePIWHh8vLy0sBAQHq0aOHTpw4YXf8vCUY+/bt0/33369SpUqpYsWKmjx5cr5633vvPdWtW1elSpVSmTJl1KRJE82fPz9frX9fcztjxgzVrVtXHh4eqlChguLi4vIFzuup4++OHj0qSWrZsmW+PhcXF5UtW1aSrvmezZkzR23btlVQUJA8PDwUFhammTNn5jtmbm6uRo8erQoVKqhUqVK6//77tW/fPlWtWtU2Q5wnNTVVQ4YMUeXKleXh4aGaNWtq0qRJys3NtRu3YMEChYeHq3Tp0vL19VX9+vX1zjvvXPPaC1K2bFktWLBArq6umjBhgq39amturVarnnrqKVWqVEkeHh4qX768HnroIdv7UrVqVe3du1cbNmywvWdt2rSRVPD9+de+q63BXrVqlRo2bChPT0+FhYXpv//9r13/6NGjrzr7//dj/lNtBa25Xbhwoe3vRbly5fTEE0/o999/txvz5JNPysfHR7///ru6du0qHx8fBQYG6oUXXlBOTs413n2g5GLmFijh0tLSdObMmXzt2dnZds979+6tfv36ac+ePXZrcRMTE3Xo0CG9+uqrduM//fRTXbhwQXFxcbp8+bLeeecdtW3bVrt375bFYpEk7d27Vy1btlTFihX10ksvydvbW19++aW6du2qRYsW6eGHH7Y75sCBAxUYGKhRo0bp4sWL6tixow4dOqTPP/9cU6dOVbly5SRJgYGBkqQJEyZo5MiR6t69u55++mmdPn1a7733nlq1aqUdO3bI39/fduzz58+rQ4cO6tatm7p3766vvvpKI0aMUP369dWxY0dJ0kcffaTnnntOjzzyiAYPHqzLly/r559/1pYtW/T4448X+B6PHj1aY8aMUWRkpAYMGKCDBw9q5syZSkxM1MaNG+Xm5nZddVxNlSpVJEmfffaZWrZsKVfXq//z3K1bt398z2bOnKm6deuqS5cucnV11ddff62BAwcqNzdXcXFxtuPEx8dr8uTJ6ty5s6KiorRr1y5FRUXp8uXLdue7dOmSWrdurd9//13//ve/FRISok2bNik+Pl6nTp3StGnTJEmrV69Wz5491a5dO02aNEmStH//fm3cuFGDBw8u8LqvJSQkRK1bt9a6deuUnp4uX1/fq46LiYnR3r179eyzz6pq1apKSUnR6tWrlZSUpKpVq2ratGl6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kUGDBsnb21uRkZHq37+/Ll26pP/85z9q3769o0uDyeSt9160aJFGjx6tnj176uWXX3Z0WaZCuMV1u3z5svbv36+ffvpJHh4ezNriljp69Ki6du2qX375Re+++6769u3r6JJgMpcvX1b9+vV19OhRubu7a8yYMRoxYoSjy4IJnT9/XuPGjdOePXu0ZcsWTZgwQYMGDXJ0WabDVmC4bp6enmrUqJEaNWrk6FJwB3BxcVFMTIxGjBghLy8vR5cDE/L09FTVqlX1wAMPaMqUKfL09HR0STCpMmXKKCQkRH5+flq6dCn32i3CzC0A4I6Xk5MjFxcXR5eBOwDbzN16hFsAAACYBrslAAAAwDQItwAAADANwi0AAABMg3ALAAAA0yDcAgAAwDQItwAAADANwi0AAABMg3ALAA52+vRpDRgwQCEhIfLw8FBwcLCioqK0ceNGSZKTk5OWLFni2CIBoITg63cBwMFiYmKUlZWlTz75RNWrV1dycrLWrFmjs2fPOro0AChxmLkFAAdKTU3VDz/8oEmTJun+++9XlSpV1KxZM8XHx6tLly6qWrWqJOnhhx+Wk5OT7fnRo0f10EMPyWKxyMfHR02bNtV3331nd+xTp04pOjpaXl5eqlatmubPn6+qVatq2rRpdud/+umnFRgYKF9fX7Vt21a7du2y9e/atUv333+/SpcuLV9fX4WHh2vbtm23+m0BgCIj3AKAA/n4+MjHx0dLlixRZmZmvv7ExERJ0pw5c3Tq1Cnb84yMDHXq1Elr1qzRjh071KFDB3Xu3FlJSUm21/bp00cnT57U+vXrtWjRIn344YdKSUmxO/6jjz6qlJQULV++XNu3b1fjxo3Vrl07nTt3TpLUq1cvVapUSYmJidq+fbteeuklubm53aq3AwBumJNhGIajiwCAO9miRYvUr18//fHHH2rcuLFat26tHj16qEGDBpL+XHO7ePFide3a9R+PU69ePT3zzDMaNGiQDhw4oDp16igxMVFNmjSRJB05ckS1atXS1KlTNWTIEP3444+Kjo5WSkqKPDw8bMepWbOmXnzxRfXv31++vr567733FBsbe8uuHwBuJmZuAcDBYmJidPLkSS1dulQdOnTQ+vXr1bhxY82dO7fA12RkZOiFF15QnTp15O/vLx8fH+3fv982c3vw4EG5urqqcePGttfUrFlTZcqUsT3ftWuXMjIyVLZsWdsMso+Pj44dO6ajR49KkoYNG6ann35akZGReuONN2ztAHC7ItwCwG3A09NTDzzwgEaOHKlNmzbpySef1GuvvVbg+BdeeEGLFy/W66+/rh9++EE7d+5U/fr1lZWVVehzZmRkqHz58tq5c6fd4+DBgxo+fLgkafTo0dq7d6+io6O1du1ahYWFafHixTd8vQBwq7BbAgDchsLCwmzbf7m5uSknJ8euf+PGjXryySf18MMPS/ozqB4/ftzWf9ddd+nKlSvasWOHwsPDJf25LOH8+fO2MY0bN5bVapWrq6vtg2pXU7t2bdWuXVtDhw5Vz549NWfOHNt5AeB2w8wtADjQ2bNn1bZtW82bN08///yzjh07poULF2ry5Ml66KGHJElVq1bVmjVrZLVabeG0Vq1a+u9//6udO3dq165devzxx5Wbm2s7bmhoqCIjI9W/f39t3bpVO3bsUP/+/eXl5SUnJydJUmRkpCIiItS1a1etWrVKx48f16ZNm/TKK69o27Zt+uOPPzRo0CCtX79ev/76qzZu3KjExETVqVOn+N8oACgkwi0AOJCPj4+aN2+uqVOnqlWrVqpXr55Gjhypfv366f3335ckvf3221q9erUqV66sRo0aSZKmTJmiMmXK6J577lHnzp0VFRVlt75Wkj799FNZLBa1atVKDz/8sPr166fSpUvL09NT0p8fVPv222/VqlUrPfXUU6pdu7Z69OihX3/9VRaLRS4uLjp79qz69Omj2rVrq3v37urYsaPGjBlTvG8SAFwHdksAgDvEb7/9psqVK+u7775Tu3btHF0OANwShFsAMKm1a9cqIyND9evX16lTp/Tiiy/q999/16FDh9irFoBp8YEyADCp7Oxsvfzyy/rll19UunRp3XPPPfrss88ItgBMjZlbAAAAmAYfKAMAAIBpEG4BAABgGoRbAAAAmAbhFgAAAKZBuAUAAIBpEG4BAABgGoRbAAAAmAbhFgAAAKZBuAUAAIBp/D/IPUhAnv1gXQAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**3. Correlation between Systolic and Diastolic Pressure**"
      ],
      "metadata": {
        "id": "wROzRrLRRj5C"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def range_to_midpoint(val):\n",
        "\n",
        "    if isinstance(val, str):\n",
        "        if \"-\" in val:\n",
        "            start, end = val.split(\"-\")\n",
        "            return (int(start.strip()) + int(end.strip())) / 2\n",
        "\n",
        "        elif \"+\" in val:\n",
        "            return int(val.replace(\"+\",\"\").strip())\n",
        "\n",
        "    return np.nan\n",
        "\n",
        "data['Systolic_num'] = data['Systolic'].apply(range_to_midpoint)\n",
        "data['Diastolic_num'] = data['Diastolic'].apply(range_to_midpoint)\n",
        "\n",
        "plt.figure(figsize=(6,4))\n",
        "\n",
        "sns.heatmap(\n",
        "    data[['Systolic_num','Diastolic_num']].corr(),\n",
        "    annot=True,\n",
        "    cmap=\"Blues\"\n",
        ")\n",
        "\n",
        "plt.title(\"Correlation between Systolic & Diastolic\")\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 426
        },
        "id": "Zv5PAux8QmtX",
        "outputId": "0f4a49ea-b2f0-4750-91d1-d0b4f2089274"
      },
      "execution_count": 202,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.12/dist-packages/seaborn/matrix.py:202: RuntimeWarning: All-NaN slice encountered\n",
            "  vmin = np.nanmin(calc_data)\n",
            "/usr/local/lib/python3.12/dist-packages/seaborn/matrix.py:207: RuntimeWarning: All-NaN slice encountered\n",
            "  vmax = np.nanmax(calc_data)\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 600x400 with 2 Axes>"
            ],
            "image/png": "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4MGD6NOnj0aCIyIiehBzAe1QacxAv379kJeXV628oKAA/fr1UzsoIiIiZThmQDtUSgaEEEpP6s2bN2FkZKR2UERERPT41OsyQdWTC2UyGUJDQxWev1xRUYFTp07By8tLsxESERH9P/641456JQNVTy4UQsDExERhsKCenh569OhRbRwBERGRprCrXzvqlQxUPbnQzs4O06dP5yUBIiJ6rJgLaIdKdxPMmDEDD85ifOnSJXz//fdwcnJC//79NRYcERHRg9gzoB0qDSAcOnQo1q9fDwDIz8+Hu7s7lixZgqFDh2LFihUaDZCIiKgKH1SkHSolA2lpaejduzcAYNu2bbC1tcWlS5ewfv16LFu2TKMBEhERkXapdJng7t27MDExAQD8/PPPGDZsGORyOXr06IFLly5pNEAiIqIqvEygHSr1DLRv3x47duzAP//8g59++kkaJ3D9+nWYmppqNEAiIqIqvEygHSolA/PmzcP06dNhZ2cHDw8P6UmFP//8M55//nmNBkhERFSFMxBqh0qXCYYPH45evXrh2rVr0lMLAcDHxwcvvfSSxoIjIiJ6EL/PtUOlZGDNmjUYNWoUbG1tFcrd3d01EhQREZEy/HWvHSpdJpg5cyZsbGwQFhaGI0eOaDomIiIieoxUSgauXLmCdevWITc3F3379kWnTp2waNEiZGdnazo+IiIiCccMaIdKyUCTJk3w0ksv4YcffsA///yD8PBwbNy4EW3atMGQIUPwww8/oLKyUtOxEhFRI/e47yb47LPPYGdnBwMDA3h4eODYsWO11o+Li0OnTp1gYGAAZ2dn7NmzR1pXVlaGd999F87OzjAyMkLLli0xZswYXL16VaENOzu7aknMhx9+WP/g60GlZOBBNjY26NWrFzw9PSGXy/H7778jJCQEDg4OSE5O1kCIRERE9z3OnoEtW7YgMjISUVFRSEtLQ9euXeHn54fr168rrX/kyBGMHj0aYWFh+O233xAYGIjAwECcPn0awP05etLS0jB37lykpaVh+/btyMzMxJAhQ6q1tWDBAly7dk1aJk6cWP+TVQ8y8eBDBuohJycH33zzDdasWYO///4bgYGBCAsLg6+vL4qKirBgwQJs3ryZkxAREZHG9PtEvXFqSZO96lzXw8MD3bt3x/LlywEAlZWVaN26NSZOnIiZM2dWqz9y5EgUFRVh165dUlmP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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**4. TakeMedication vs. Severity**"
      ],
      "metadata": {
        "id": "X5dT2XmQRovh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(8,5))\n",
        "\n",
        "sns.countplot(\n",
        "    data=data,\n",
        "    x=\"TakeMedication\",\n",
        "    hue=\"Severity\",\n",
        "    palette=\"Set1\"\n",
        ")\n",
        "\n",
        "plt.title(\"TakeMedication vs Severity\")\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 315
        },
        "id": "mouY54q_RBMp",
        "outputId": "bbcbe077-e187-4593-9ed2-6bb0971c4d73"
      },
      "execution_count": 203,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x500 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAArcAAAHWCAYAAABt3aEVAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAASaJJREFUeJzt3XlYVdUe//HPYQYRCGVURDRNMUecaHBEEY1rV8shSyWz8mI3o8zo5pQVZYOamd7qplZSaqmlOZNDzkNppmZqmPZTQC1BMEFh//7o5/51AidEDu7er+fZz+Nea+29v/ucHvqwWGcfm2EYhgAAAAALcHJ0AQAAAEBZIdwCAADAMgi3AAAAsAzCLQAAACyDcAsAAADLINwCAADAMgi3AAAAsAzCLQAAACyDcAsAAADLINwCuO5q1qypu+66y9FlXLOaNWtq4MCB5v7q1atls9m0evVqh9eCiqFdu3Zq166do8sA/tYItwBKZLPZrmgr72A3Y8YM89rr1q0r1m8YhsLCwmSz2W74QL1hwwaNGTNGp06dcnQp5WrdunWKi4tTtWrV5OHhoRo1aig+Pl6pqamOLu2qHT16VGPGjNGOHTscXQrwt+Hi6AIAVEwffvih3f4HH3ygFStWFGuvX79+eZZl8vDwUGpqqu644w679jVr1uiXX36Ru7v7da+hTZs2+v333+Xm5nZdzr9hwwaNHTtWAwcOlJ+fn13fvn375ORkvfmJuXPnqnfv3mrSpIkef/xx3XTTTUpPT9fatWv17rvv6r777nN0iZe0fPlyu/2jR49q7Nixqlmzppo0aeKYooC/GcItgBLdf//9dvubNm3SihUrirU7SteuXTV37ly9+eabcnH5/z/KUlNTFRUVpRMnTlz3GpycnOTh4XHdr1OS8gjvjjBmzBhFRkZq06ZNxX5pyMrKclBVl3fmzBl5eXldt190AFw56/3aD6DcTJ8+XR06dFBgYKDc3d0VGRmpqVOnXtGxM2fOlIuLi4YPH262bd68WV26dJGvr6+8vLzUtm1brV+/vsTj+/btq5MnT2rFihVmW0FBgT799NOLzu4VFRVp4sSJatCggTw8PBQUFKRHHnlEv/32m904wzD0wgsvqHr16vLy8lL79u21e/fuYue72JrbzZs3q2vXrrrppptUqVIlNWrUSJMmTTL7v/vuOw0cOFC1atWSh4eHgoOD9eCDD+rkyZPmmDFjxpivTUREhLkU49ChQ5JKXnP7008/6d5775W/v7+8vLzUunVrffnllyXWPGfOHL344ouqXr26PDw81LFjRx04cKDE1+2CTz/9VDabTWvWrCnW99///lc2m03ff/+9JCkjI0MJCQmqXr263N3dFRISou7du5v1X8zBgwfVokWLEkNiYGCg3f6VvJ933XWXatWqVeK1oqOj1bx5c7u2jz76SFFRUfL09JS/v7/69OmjI0eO2I1p166dbr31Vm3fvl1t2rSRl5eXnn32WbPvwprb1atXq0WLFpKkhIQE8z2cMWOGRo8eLVdXVx0/frxYXQ8//LD8/Px09uzZS75WAEpGuAVQalOnTlV4eLieffZZvf766woLC9O//vUvTZky5ZLHvfPOO0pISNAzzzyjV199VZL01VdfqU2bNsrJydHo0aP10ksv6dSpU+rQoYO2bNlS7Bw1a9ZUdHS0Pv74Y7NtyZIlys7OVp8+fUq87iOPPKLhw4fr9ttv16RJk5SQkKBZs2YpNjZW586dM8eNGjVKI0eOVOPGjfXqq6+qVq1a6ty5s/Ly8i77mqxYsUJt2rTRnj179Pjjj+v1119X+/bttWjRIrsxP/30kxISEjR58mT16dNHn3zyibp27SrDMCRJPXr0UN++fSVJEyZM0IcffqgPP/xQAQEBJV43MzNTt912m5YtW6Z//etfevHFF3X27Fn94x//0Pz584uNf/nllzV//nw99dRTSk5O1qZNm9SvX79L3lu3bt3k7e2tOXPmFOubPXu2GjRooFtvvVWS1LNnT82fP18JCQl6++239e9//1unT5/W4cOHL3mN8PBwpaWl6ZdffrnkOOnK3s/evXsrPT1dW7dutTv2559/1qZNm+z+W3nxxRfVv39/1alTR2+88YaGDRumtLQ0tWnTpti655MnTyouLk5NmjTRxIkT1b59+2L11a9fX88//7ykPwLrhfewTZs2euCBB3T+/HnNnj3b7pgLv6D17NnTYX8VAG54BgBcgcTEROOvPzLOnDlTbFxsbKxRq1Ytu7bw8HCjW7duhmEYxqRJkwybzWaMGzfO7C8qKjLq1KljxMbGGkVFRXbnj4iIMDp16mS2TZ8+3ZBkbN261XjrrbeMypUrm3Xce++9Rvv27Ytd0zAM4+uvvzYkGbNmzbKrbenSpXbtWVlZhpubm9GtWze7Wp599llDkjFgwACzbdWqVYYkY9WqVYZhGMb58+eNiIgIIzw83Pjtt9/srvPX+/qrjz/+2JBkrF271mx79dVXDUlGenp6sfHh4eF2tQwbNsyQZHz99ddm2+nTp42IiAijZs2aRmFhoV3N9evXN/Lz882xkyZNMiQZu3btKnatP+vbt68RGBhonD9/3mw7duyY4eTkZDz//POGYRjGb7/9ZkgyXn311UueqyT/+9//DEmGm5ub0b59e2PkyJHG119/bdZ/wZW+n9nZ2Ya7u7vx5JNP2o0bP368YbPZjJ9//tkwDMM4dOiQ4ezsbLz44ot243bt2mW4uLjYtbdt29aQZEybNq1Y/W3btjXatm1r7m/dutWQZEyfPr3Y2OjoaKNVq1Z2bfPmzbP7bwrA1WPmFkCpeXp6mv/Ozs7WiRMn1LZtW/3000/Kzs4uNn78+PF6/PHH9corr+i5554z23fs2KH9+/frvvvu08mTJ3XixAmdOHFCeXl56tixo9auXauioqJi5+vVq5d+//13LVq0SKdPn9aiRYsuuiRh7ty58vX1VadOnczznzhxQlFRUfL29taqVaskSStXrlRBQYEee+wx2Ww28/hhw4Zd9vX49ttvlZ6ermHDhhX7ANifz/Xn1+3s2bM6ceKEWrduLUn65ptvLnudkixevFgtW7a0+4Cdt7e3Hn74YR06dEh79uyxG5+QkGD3p/8777xT0h9LGy6ld+/eysrKsluK8emnn6qoqEi9e/c278/NzU2rV68utuTjch588EEtXbpU7dq107p16zRu3DjdeeedqlOnjjZs2GCOu9L308fHR3FxcZozZ445Ky79MdPcunVr1ahRQ5I0b948FRUVqVevXnbnCw4OVp06dczzXeDu7q6EhISrure/6t+/vzZv3qyDBw+abbNmzVJYWJjatm17TecG/s4ItwBKbf369YqJiVGlSpXk5+engIAAc+3hX8PtmjVrNGLECI0YMcJuna0k7d+/X5I0YMAABQQE2G3vvfee8vPzSwzLAQEBiomJUWpqqubNm6fCwkLdc889Jda6f/9+ZWdnKzAwsNg1cnNzzQ8r/fzzz5KkOnXqFLvWTTfddMnX40JIufCn+Yv59ddf9fjjjysoKEienp4KCAhQRESEpOKv25X6+eefdcsttxRrv/A0iwv3dcGFUHfBhXu7XBi9sCb6z39Onz17tpo0aaK6detK+iP4vfLKK1qyZImCgoLUpk0bjR8/XhkZGVd0L7GxsVq2bJlOnTqltWvXKjExUT///LPuuusu83260vdT+iOQHzlyRBs3bpT0x/u0fft2M4xfOJ9hGKpTp06x8+3du7fYh9mqVat2zR8e6927t9zd3TVr1ixJf7z3ixYtUr9+/ex+GQJwdXhaAoBSOXjwoDp27Kh69erpjTfeUFhYmNzc3LR48WJNmDCh2ExrgwYNdOrUKX344Yd65JFHzDAnyRz76quvXvRxSd7e3iW233fffRo8eLAyMjIUFxdXbMb0z9cIDAw0g8RfXWwt6/XQq1cvbdiwQcOHD1eTJk3k7e2toqIidenSpcQZ6uvB2dm5xPY/z26WxN3dXXfffbfmz5+vt99+W5mZmVq/fr1eeuklu3HDhg1TfHy8FixYoGXLlmnkyJFKSUnRV199paZNm15RjV5eXrrzzjt15513qmrVqho7dqyWLFmiAQMGXNX7GR8fLy8vL82ZM0e33Xab5syZIycnJ917773mmKKiItlsNi1ZsqTE1+av//39efa9tG666SbdddddmjVrlkaNGqVPP/1U+fn5FeaJJMCNinALoFQWLlyo/Px8ffHFF3azgH/98+0FVatW1aeffqo77rhDHTt21Lp16xQaGipJql27tqQ//oQcExNzVXX885//1COPPKJNmzYV+3DOn9WuXVsrV67U7bfffslgEh4eLumPmbw/f8r++PHjl53VvHAf33///UXv47ffflNaWprGjh2rUaNGme0XZq//7Gpm78LDw7Vv375i7T/88IPZX1Z69+6tmTNnKi0tTXv37pVhGHazoBfUrl1bTz75pJ588knt379fTZo00euvv66PPvroqq954akGx44dM899Je+nJFWqVEl33XWX5s6dqzfeeEOzZ8/WnXfeaf73d+F8hmEoIiLCnIEuC5d7D/v376/u3btr69atmjVrlpo2baoGDRqU2fWBvyOWJQAolQuzW3+e6cvOztb06dMvekz16tW1cuVK/f777+rUqZP56KuoqCjVrl1br732mnJzc4sdV9Ljki7w9vbW1KlTNWbMGMXHx190XK9evVRYWKhx48YV6zt//rz5afiYmBi5urpq8uTJdvc2ceLEi577gmbNmikiIkITJ04s9un6C+cq6XW72PkrVaokSVf0DWVdu3bVli1bzD+9S1JeXp7eeecd1axZU5GRkZc9x5WKiYmRv7+/Zs+erdmzZ6tly5Z2M/Fnzpwp9hir2rVrq3LlysrPz7/kudPS0kpsX7x4sSSZSy+u9P28oHfv3jp69Kjee+897dy5s1gY79Gjh5ydnTV27Nhi741hGHaPabsal3sP4+LiVLVqVb3yyitas2YNs7ZAGWDmFkCpdO7cWW5uboqPj9cjjzyi3NxcvfvuuwoMDDRn10py8803a/ny5WrXrp1iY2P11VdfycfHR++9957i4uLUoEEDJSQkqFq1avo//+f/aNWqVfLx8dHChQsves4BAwZctt62bdvqkUceUUpKinbs2KHOnTvL1dVV+/fv19y5czVp0iTdc889CggI0FNPPaWUlBTddddd6tq1q7799lstWbJEVatWveQ1nJycNHXqVMXHx6tJkyZKSEhQSEiIfvjhB+3evVvLli2Tj4+PuQb13LlzqlatmpYvX6709PRi54uKipIk/ec//1GfPn3k6uqq+Ph4MzD92TPPPKOPP/5YcXFx+ve//y1/f3/NnDlT6enp+uyzz8r028xcXV3Vo0cPffLJJ8rLy9Nrr71m1//jjz+qY8eO6tWrlyIjI+Xi4qL58+crMzPzoo9pu6B79+6KiIhQfHy8ateurby8PK1cuVILFy5UixYtzF9grvT9vKBr166qXLmynnrqKTk7O6tnz552161du7ZeeOEFJScn69ChQ7r77rtVuXJlpaena/78+Xr44Yf11FNPXfVrVbt2bfn5+WnatGmqXLmyKlWqpFatWpm/DLi6uqpPnz5666235OzsbD7+DcA1cNBTGgDcYEp6FNgXX3xhNGrUyPDw8DBq1qxpvPLKK8b7779f7PFVf30sl2EYxubNm43KlSsbbdq0MR+N9e233xo9evQwqlSpYri7uxvh4eFGr169jLS0NPO4Pz8K7FJKuqZhGMY777xjREVFGZ6enkblypWNhg0bGk8//bRx9OhRc0xhYaExduxYIyQkxPD09DTatWtnfP/998Uev/XXR4FdsG7dOqNTp05G5cqVjUqVKhmNGjUyJk+ebPb/8ssvxj//+U/Dz8/P8PX1Ne69917j6NGjhiRj9OjRducaN26cUa1aNcPJycnudf1rLYZhGAcPHjTuuecew8/Pz/Dw8DBatmxpLFq0yG7MhZrnzp1r156enn7RR1aVZMWKFYYkw2azGUeOHLHrO3HihJGYmGjUq1fPqFSpkuHr62u0atXKmDNnzmXP+/HHHxt9+vQxateubXh6ehoeHh5GZGSk8Z///MfIyckpNv5K3s8L+vXrZ0gyYmJiLnr9zz77zLjjjjuMSpUqGZUqVTLq1atnJCYmGvv27TPHtG3b1mjQoEGJx//1UWCGYRiff/65ERkZabi4uJT4Gm/ZssWQZHTu3PkSrwyAK2UzjMt8egAAAFw3O3fuVJMmTfTBBx/ogQcecHQ5wA2PNbcAADjQu+++K29vb/Xo0cPRpQCWwJpbAAAcYOHChdqzZ4/eeecdDR06tMS11ACuHssSAABwgJo1ayozM1OxsbH68MMPVblyZUeXBFgC4RYAAACWwZpbAAAAWAbhFgAAAJbBB8r0x3eKHz16VJUrV76qr7sEAABA+TAMQ6dPn1ZoaOglv5iGcCvp6NGjCgsLc3QZAAAAuIwjR46oevXqF+0n3ErmJ1SPHDkiHx8fB1cDAACAv8rJyVFYWNhlnyxCuJXMpQg+Pj6EWwAAgArscktI+UAZAAAALINwCwAAAMsg3AIAAMAyWHN7hQoLC3Xu3DlHl1GhODs7y8XFhcenAQCACoNwewVyc3P1yy+/iG8qLs7Ly0shISFyc3NzdCkAAACE28spLCzUL7/8Ii8vLwUEBDBL+f8YhqGCggIdP35c6enpqlOnziUfqAwAAFAeCLeXce7cORmGoYCAAHl6ejq6nArF09NTrq6u+vnnn1VQUCAPDw9HlwQAAP7mmGq7QszYlozZWgAAUJGQTAAAAGAZhFsAAABYBuH2b8Bms2nBggWOLgMAAOC6I9yWkePHj2vIkCGqUaOG3N3dFRwcrNjYWK1fv97RpenYsWOKi4uTJB06dEg2m007duxwbFEAAADXAU9LKCM9e/ZUQUGBZs6cqVq1aikzM1NpaWk6efKkw2oqKCiQm5ubgoODHVYDAABAeWLmtgycOnVKX3/9tV555RW1b99e4eHhatmypZKTk/WPf/zDHPPQQw8pICBAPj4+6tChg3bu3ClJ+vHHH2Wz2fTDDz/YnXfChAmqXbu2uf/9998rLi5O3t7eCgoK0gMPPKATJ06Y/e3atdPQoUM1bNgwVa1aVbGxsZLslyVERERIkpo2bSqbzaZ27dpp7dq1cnV1VUZGht31hw0bpjvvvLNsXywAAIDriHBbBry9veXt7a0FCxYoPz+/xDH33nuvsrKytGTJEm3fvl3NmjVTx44d9euvv6pu3bpq3ry5Zs2aZXfMrFmzdN9990n6Ixx36NBBTZs21bZt27R06VJlZmaqV69edsfMnDlTbm5uWr9+vaZNm1asji1btkiSVq5cqWPHjmnevHlq06aNatWqpQ8//NAcd+7cOc2aNUsPPvjgNb02AAAA5YllCWXAxcVFM2bM0ODBgzVt2jQ1a9ZMbdu2VZ8+fdSoUSOtW7dOW7ZsUVZWltzd3SVJr732mhYsWKBPP/1UDz/8sPr166e33npL48aNk/THbO727dv10UcfSZLeeustNW3aVC+99JJ53ffff19hYWH68ccfVbduXUlSnTp1NH78+IvWGhAQIEmqUqWK3XKFQYMGafr06Ro+fLgkaeHChTp79myx8AwAKD9dRs52dAmW4V93vqNLsIzUBz5xdAmXxMxtGenZs6eOHj2qL774Ql26dNHq1avVrFkzzZgxQzt37lRubq6qVKlizvJ6e3srPT1dBw8elCT16dNHhw4d0qZNmyT9MWvbrFkz1atXT5K0c+dOrVq1yu74C30XziFJUVFRpap/4MCBOnDggHn9GTNmqFevXqpUqVKpXxMAAIDyxsxtGfLw8FCnTp3UqVMnjRw5Ug899JBGjx6tf/3rXwoJCdHq1auLHePn5ydJCg4OVocOHZSamqrWrVsrNTVVQ4YMMcfl5uYqPj5er7zySrFzhISEmP8ubRgNDAxUfHy8pk+froiICC1ZsqTEegEAACoywu11FBkZqQULFqhZs2bKyMiQi4uLatasedHx/fr109NPP62+ffvqp59+Up8+fcy+Zs2a6bPPPlPNmjXl4lL6t83NzU2SVFhYWKzvoYceUt++fVW9enXVrl1bt99+e6mvAwAA4AgsSygDJ0+eVIcOHfTRRx/pu+++U3p6uubOnavx48ere/fuiomJUXR0tO6++24tX75chw4d0oYNG/Sf//xH27ZtM8/To0cPnT59WkOGDFH79u0VGhpq9iUmJurXX39V3759tXXrVh08eFDLli1TQkJCiUH1YgIDA+Xp6Wl+IC07O9vsi42NlY+Pj1544QUlJCSUzYsDAABQjgi3ZcDb21utWrXShAkT1KZNG916660aOXKkBg8erLfeeks2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XrVq1cquPzo6+pL3uWPHDg0ePPii/du3b9eYMWO0c+dO/fbbbyoqKpIkHT58WJGRkZc89wV79+6Vi4uLXW1VqlTRLbfcor1795ptXl5eql27trkfEhJiLoEAgMsh3ALAJTz11FNasWKFXnvtNd18883y9PTUPffco4KCArtxd955p7788kvNmTPHbglAbm6u4uPj9corrxQ7d0hISLG2Bx98UEOHDpUkTZkypVh/bm6upD+WEVSrVs2uz93d/epv8P+51IfL8vLyFBsbq9jYWM2aNUsBAQE6fPiwYmNji70OZcHV1dVu32azyTCMMr8OAGsi3ALAJaxfv14DBw40P1yVm5tb7MNZktSyZUsNHTpUXbp0kYuLi7lGtFmzZvrss89Us2ZNubhc/kduly5dVFBQIJvNptjY2GL9kZGRcnd31+HDh9W2bdsSz1G/fn198cUXdm2bNm265HUbNWqktLS0Etf4/vDDDzp58qRefvllhYWFSZK2bdtmN8bNzU2SVFhYeNFr1K9fX+fPn9fmzZt12223SZJOnjypffv2XfHsLwBcDh8oA4BLqFOnjubNm6cdO3Zo586duu+++8w/yf/VbbfdpsWLF2vs2LHmlzokJibq119/Vd++fbV161YdPHhQy5YtU0JCQolB0NnZWXv37tWePXvk7OxcrL9y5cp66qmn9MQTT2jmzJk6ePCgvvnmG02ePFkzZ86UJD366KPav3+/hg8frn379ik1NVUzZsy45H2OHj1aH3/8sUaPHq29e/dq165d5mxzjRo15ObmpsmTJ+unn37SF198UezZteHh4bLZbFq0aJGOHz9uzjD/9bXs3r27Bg8erHXr1mnnzp26//77Va1aNXXv3v2S9QHAlSLcAsAlvPHGG7rpppt02223KT4+XrGxsWrWrNlFx99xxx368ssv9dxzz2ny5MkKDQ3V+vXrVVhYqM6dO6thw4YaNmyY/Pz85ORU8o9gHx8f+fj4XPQa48aN08iRI5WSkqL69eurS5cu+vLLLxURESHpjzD62WefacGCBWrcuLGmTZuml1566ZL32a5dO82dO1dffPGFmjRpog4dOmjLli2S/lgLPGPGDM2dO1eRkZF6+eWX9dprr9kdX61aNY0dO1bPPPOMgoKCzKUVfzV9+nRFRUXprrvuUnR0tAzD0OLFi4stRQCA0rIZLGQCAACARTBzCwAAAMsg3AIAAMAyCLcAAACwDMItAAAALINwCwAAAMsg3AIAAMAyCLcAAACwDMItAAAALINwCwAAAMsg3AIAAMAyCLcAAACwjP8LqB3j/oHOunAAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**5. Age Group vs. Hypertension Stages**"
      ],
      "metadata": {
        "id": "SSVvUvZxRsH5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(8,5))\n",
        "\n",
        "sns.countplot(\n",
        "    data=data,\n",
        "    x=\"Age\",\n",
        "    hue=\"Stages\",\n",
        "    palette=\"husl\"\n",
        ")\n",
        "\n",
        "plt.title(\"Age Group vs Hypertension Stages\")\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 315
        },
        "id": "ZBgtmFS3RF5k",
        "outputId": "b4f0b710-7245-4101-a7dd-1521a86a7205"
      },
      "execution_count": 204,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x500 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAArcAAAHWCAYAAABt3aEVAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAUHhJREFUeJzt3XlUVWX////XkeGAICAqk+KUA2rOA5HmFIVmmmW3Q2Zapt2KlVlm3KllpaZNlplWH4f6hmmWmllp5piKA07lEKlhmgpYhgoqKFy/P1qeXyfEFIEDu+djrb1W+9rX2dd777OJl5vr7GMzxhgBAAAAFlDG1QUAAAAAhYVwCwAAAMsg3AIAAMAyCLcAAACwDMItAAAALINwCwAAAMsg3AIAAMAyCLcAAACwDMItAAAALINwCwAo9ebMmSObzaZDhw65uhQALka4BUqJd955RzabTZGRka4uRZKUlZWlqVOnqk2bNipfvrw8PT0VFhambt266eOPP1ZOTo6rSyyRLoWwxMTEy25v3769brzxxmKu6tpt3LhRzz//vNLT011distlZ2frzTffVNOmTeXn56eAgAA1aNBAgwcP1o8//ujoxzkDigfhFigl4uPjVb16dW3ZskUHDhxwaS0nTpxQ69at9dhjj8nX11ejR4/Wu+++q0cffVSZmZm67777NGHCBJfWiKK1ceNGjRs3rsQEtX79+uncuXOqVq1asY/do0cPPfnkk7rxxhv18ssva9y4cWrbtq2+/vprbdq0ydGvpJ0zwKrcXV0AgH+WnJysjRs3auHChXrkkUcUHx+v5557zmX19OvXTzt27NBnn32me+65x2lbXFycEhMTlZSUdMV9nD9/Xp6enipThn9jlyaZmZny8fFxdRl5uLm5yc3NrdjH3bp1q5YuXarx48frf//7n9O2t99+myALuAC/VYBSID4+XuXLl1eXLl107733Kj4+/rL9fv/9d/Xr18/xp9H+/ftr165dstlsmjNnjlPfH3/8Uffee68CAwPl5eWlFi1aaMmSJf9YS0JCgpYvX67BgwfnCbaXtGjRQn379nWsr1mzRjabTfPmzdPo0aNVuXJllS1bVqdPn5YkLViwQM2bN5e3t7cqVqyo+++/X0ePHnXaZ/v27dW+ffs8Yw0YMEDVq1d3rB86dEg2m02vvvqq3njjDVWrVk3e3t5q166ddu/efcVjS0xMlM1m0wcffJBn2/Lly2Wz2bR06VJJ0pkzZzR8+HBVr15ddrtdQUFBuu2227R9+/YrjnGt2rVrp8aNG192W926dRUTEyPp2o/7at7/S1Mo1q5dq6FDhyooKEhVqlTR888/r5EjR0qSatSoIZvNlme+60cffeR4TwMDA9W7d28dOXLEaf+XpmDs3btXHTp0UNmyZVW5cmVNnjw5T71Tp05VgwYNVLZsWZUvX14tWrTQ3Llz89T69zm377zzjho0aCC73a6wsDDFxsbmCZzXUsffHTx4UJLUunXrPNvc3NxUoUIFSfrHczZ79mx17NhRQUFBstvtql+/vqZPn55nn7m5uXr++ecVFhamsmXLqkOHDtq7d6+qV6+uAQMGOPVNT0/X8OHDFR4eLrvdrlq1amnSpEnKzc116jdv3jw1b95c5cqVk5+fnxo2bKg333zzH48dKKm4cwuUAvHx8brnnnvk6empPn36aPr06dq6datatmzp6JObm6uuXbtqy5YtGjJkiCIiIvT555+rf//+efa3Z88etW7dWpUrV9YzzzwjHx8fffLJJ+revbs+++wz3X333fnW8sUXX0iS7r///ms+jhdffFGenp566qmnlJWVJU9PT82ZM0cPPvigWrZsqYkTJyo1NVVvvvmmNmzYoB07diggIOCax5GkDz/8UGfOnFFsbKzOnz+vN998Ux07dtQPP/yg4ODgy76mRYsWqlmzpj755JM8523+/PkqX768I0z+97//1aeffqphw4apfv36+v3337V+/Xrt27dPzZo1+8f6Tp06pd9++y1P+4ULF5zW+/Xrp0GDBmn37t1Oc3G3bt2qn376SaNHj77m477W93/o0KGqVKmSxo4dq8zMTHXu3Fk//fSTPv74Y73xxhuqWLGiJKlSpUqSpPHjx2vMmDHq2bOnHn74YZ04cUJTp05V27Zt87ynf/zxhzp16qR77rlHPXv21KeffqpRo0apYcOG6ty5syTp/fff12OPPaZ7771Xjz/+uM6fP6/vv/9emzdv1n333ZfvOX7++ec1btw4RUdHa8iQIUpKSnL87GzYsEEeHh7XVMflXJoGER8fr9atW8vd/fK/Vu+5554rnrPp06erQYMG6tatm9zd3fXFF19o6NChys3NVWxsrGM/cXFxmjx5srp27aqYmBjt2rVLMTExOn/+vNN4Z8+eVbt27XT06FE98sgjqlq1qjZu3Ki4uDgdP35cU6ZMkSStWLFCffr00a233qpJkyZJkvbt26cNGzbo8ccfz/e4gRLNACjREhMTjSSzYsUKY4wxubm5pkqVKubxxx936vfZZ58ZSWbKlCmOtpycHNOxY0cjycyePdvRfuutt5qGDRua8+fPO9pyc3PNzTffbGrXrn3Feu6++24jyaSnpzu1nzt3zpw4ccKx/PHHH45tq1evNpJMzZo1zdmzZx3t2dnZJigoyNx4443m3LlzjvalS5caSWbs2LGOtnbt2pl27drlqad///6mWrVqjvXk5GQjyXh7e5tff/3V0b5582YjyTzxxBNXPL64uDjj4eFhTp486WjLysoyAQEB5qGHHnK0+fv7m9jY2Cvu63Jmz55tJF1xadCggaN/enq68fLyMqNGjXLaz2OPPWZ8fHxMRkbGNR/31b7/l2pt06aNuXjxotP4r7zyipFkkpOTndoPHTpk3NzczPjx453af/jhB+Pu7u7U3q5dOyPJfPjhh462rKwsExISYnr06OFou+uuu5zOyeVcqvVSPWlpacbT09PcfvvtJicnx9Hv7bffNpLMrFmzrrmOy8nNzXW8Pjg42PTp08dMmzbN/PLLL3n65nfOjDFOPxeXxMTEmJo1azrWU1JSjLu7u+nevbtTv+eff95IMv3793e0vfjii8bHx8f89NNPTn2feeYZ4+bmZg4fPmyMMebxxx83fn5+ed5foDRjWgJQwsXHxys4OFgdOnSQJNlsNvXq1Uvz5s1zeiLBsmXL5OHhoUGDBjnaypQp43TXR5JOnjypVatWqWfPnjpz5ox+++03/fbbb/r9998VExOj/fv355kS8FeXphL4+vo6tc+YMUOVKlVyLG3atMnz2v79+8vb29uxnpiYqLS0NA0dOlReXl6O9i5duigiIkJffvnl1Zyiy+revbsqV67sWG/VqpUiIyP11VdfXfF1vXr10oULF7Rw4UJH2zfffKP09HT16tXL0RYQEKDNmzfr2LFjBapv2rRpWrFiRZ6lUaNGTv38/f1111136eOPP5YxRpKUk5Oj+fPnq3v37nnmv/7TcRfk/R80aNBVz2dduHChcnNz1bNnT8e+f/vtN4WEhKh27dpavXq1U39fX1+nvwJ4enqqVatW+vnnnx1tAQEB+vXXX7V169arqkGSvv32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KLDq1avriSeecPR96KGH9PrrrysmJkYDBw5UWlqaZsyYoQYNGjg+5PZXtWrVUps2bTRkyBBlZWVpypQpqlChQr5/pv27Xr16aezYsfLy8tLAgQOdPpR05swZValSRffee68aN24sX19fffvtt9q6datee+21q9r/tWratKluvPFGLViwQPXq1cv3cWNXc9zX+/5LUvPmzSVJzz77rHr37i0PDw917dpVN9xwg1566SXFxcXp0KFD6t69u8qVK6fk5GQtWrRIgwcP1lNPPXVNx3777bcrJCRErVu3VnBwsPbt26e3335bXbp0ccwB/7tKlSopLi5O48aNU6dOndStWzclJSXpnXfeUcuWLQv0KLvL2bVrl+677z517txZt9xyiwIDA3X06FF98MEHOnbsmKZMmeIIr/mds9tvv91x9/TSP17ef/99BQUFOf0DJDg4WI8//rhee+01devWTZ06ddKuXbv09ddfq2LFik4/4yNHjtSSJUt05513asCAAWrevLkyMzP1ww8/6NNPP9WhQ4dUsWJFPfzwwzp58qQ6duyoKlWq6JdfftHUqVPVpEkT1atXr1DOEVDsXPGIBgD/rGvXrsbLy8tkZmbm22fAgAHGw8PD/Pbbb8YYY06cOGHuu+8+U65cOePv728GDBhgNmzYYCSZefPmOb324MGD5oEHHjAhISHGw8PDVK5c2dx5553m008/var6zp07Z6ZMmWKioqKMn5+fcXd3NyEhIebOO+808fHxTo8WuvQosAULFlx2X/PnzzdNmzY1drvdBAYGmr59+zo9zuqSjz76yNSsWdN4enqaJk2amOXLl+f7KLBXXnnFvPbaayY8PNzY7XZzyy23mF27dl3VsRljzP79+x2P5lq/fr3TtqysLDNy5EjTuHFjU65cOePj42MaN25s3nnnnX/c76VHVm3duvWy29u1a5fvY68mT55sJJkJEybk2Xatx3017/8/1friiy+aypUrmzJlyuR5xNVnn31m2rRpY3x8fIyPj4+JiIgwsbGxJikp6R+P9e/v6bvvvmvatm1rKlSoYOx2u7nhhhvMyJEjzalTp/LU+vfHbL399tsmIiLCeHh4mODgYDNkyBCnx9RdSx2Xk5qaal5++WXTrl07Exoaatzd3U358uVNx44dL/uzlN85W7JkiWnUqJHx8vIy1atXN5MmTTKzZs3Kc0wXL140Y8aMMSEhIcbb29t07NjR7Nu3z1SoUMH897//dRrrzJkzJi4uztSqVct4enqaihUrmptvvtm8+uqrJjs72xhjzKeffmpuv/12ExQUZDw9PU3VqlXNI488Yo4fP37F4wZKMpsx1zhbHkCpsnjxYt19991av379dc+RLQ0OHTqkGjVq6JVXXrnmO4Ql3ZtvvqknnnhChw4dcpqbKVn7uHFl6enpKl++vF566SU9++yzri4HcDnm3AIWcu7cOaf1nJwcTZ06VX5+flf1rVkouYwxmjlzptq1a5cn2OLf4+8/45Ic3zZ2ua+nBv6NmHMLWMijjz6qc+fOKSoqSllZWVq4cKE2btyoCRMmXNdjuOA6mZmZWrJkiVavXq0ffvgh3w/x4d9h/vz5mjNnju644w75+vpq/fr1+vjjj3X77bf/K/4yA1wNwi1gIR07dtRrr72mpUuX6vz586pVq5amTp161Q+SR8lz4sQJ3XfffQoICND//ve/fD9giH+HRo0ayd3dXZMnT9bp06cdHzJ76aWXXF0aUGIw5xYAAACWwZxbAAAAWAbhFgAAAJbBnFv9+S1Ox44dU7ly5fL9ekQAAAC4jjFGZ86cUVhYmNMX6/wd4VbSsWPHFB4e7uoyAAAA8A+OHDmiKlWq5LudcCs5vr7xyJEj8vPzc3E1AAAA+LvTp08rPDw836/dvoRwKzmmIvj5+RFuAQAASrB/mkLKB8oAAABgGYRbAAAAWAbhFgAAAJbBnFsAAIBSwBijixcvKicnx9WlFAk3Nze5u7tf92NZCbcAAAAlXHZ2to4fP66zZ8+6upQiVbZsWYWGhsrT07PA+yDcAgAAlGC5ublKTk6Wm5ubwsLC5OnpabkvnTLGKDs7WydOnFBycrJq1659xS9quBLCLQAAQAmWnZ2t3NxchYeHq2zZsq4up8h4e3vLw8NDv/zyi7Kzs+Xl5VWg/fCBMgAAgFKgoHcyS5PCOEbrnyUAAAD8axBuAQAAYBmEWwAAAFgG4RYAAKAUO3HihIYMGaKqVavKbrcrJCREMTEx2rBhgyTJZrNp8eLFri2yGPG0BAAAgFKsR48eys7O1gcffKCaNWsqNTVVK1eu1O+//+7q0lyCO7cAAAClVHp6ur777jtNmjRJHTp0ULVq1dSqVSvFxcWpW7duql69uiTp7rvvls1mc6wfPHhQd911l4KDg+Xr66uWLVvq22+/ddr38ePH1aVLF3l7e6tGjRqaO3euqlevrilTpjiN//DDD6tSpUry8/NTx44dtWvXLsf2Xbt2qUOHDipXrpz8/PzUvHlzJSYmFuk5IdwCAACUUr6+vvL19dXixYuVlZWVZ/vWrVslSbNnz9bx48cd6xkZGbrjjju0cuVK7dixQ506dVLXrl11+PBhx2sfeOABHTt2TGvWrNFnn32m9957T2lpaU77/89//qO0tDR9/fXX2rZtm5o1a6Zbb71VJ0+elCT17dtXVapU0datW7Vt2zY988wz8vDwKKrTIYlpCaVe3w87umzs+AdWuWxsFD+uNRQXrjUUFytca+7u7pozZ44GDRqkGTNmqFmzZmrXrp169+6tRo0aqVKlSpKkgIAAhYSEOF7XuHFjNW7c2LH+4osvatGiRVqyZImGDRumH3/8Ud9++622bt2qFi1aSJL+7//+T7Vr13a8Zv369dqyZYvS0tJkt9slSa+++qoWL16sTz/9VIMHD9bhw4c1cuRIRURESJLT64sKd24BAABKsR49eujYsWNasmSJOnXqpDVr1qhZs2aaM2dOvq/JyMjQU089pXr16ikgIEC+vr7at2+f485tUlKS3N3d1axZM8dratWqpfLlyzvWd+3apYyMDFWoUMFxB9nX11fJyck6ePCgJGnEiBF6+OGHFR0drZdfftnRXpQItwAAAKWcl5eXbrvtNo0ZM0YbN27UgAED9Nxzz+Xb/6mnntKiRYs0YcIEfffdd9q5c6caNmyo7Ozsqx4zIyNDoaGh2rlzp9OSlJSkkSNHSpKef/557dmzR126dNGqVatUv359LVq06LqP90qYlgAAAGAx9evXdzz+y8PDQzk5OU7bN2zYoAEDBujuu++W9GdQPXTokGN73bp1dfHiRe3YsUPNmzeXJB04cEB//PGHo0+zZs2UkpIid3d3xwfVLqdOnTqqU6eOnnjiCfXp00ezZ892jFsUuHMLAABQSv3+++/q2LGjPvroI33//fdKTk7WggULNHnyZN11112SpOrVq2vlypVKSUlxhNPatWtr4cKF2rlzp3bt2qX77rtPubm5jv1GREQoOjpagwcP1pYtW7Rjxw4NHjxY3t7estlskqTo6GhFRUWpe/fu+uabb3To0CFt3LhRzz77rBITE3Xu3DkNGzZMa9as0S+//KINGzZo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wYMHncaR5NTn2LFjysjIcOpTpkwZValS5V99bi5Zu3atDhw4oIEDBwqFh9+hhczVt45RMs2bN8/Y7XYzZ84cs3fvXjN48GATEBBgUlJSjDHG9OvXz/GnMWP+/BOau7u7efXVV82+ffvMc889x6PA/sG1nuMJEyaYb775xhw8eNDs3bvXvPrqq8bd3d28//77xpg//9QdFxfneIRUYmKiefDBB43dbje7d+82xhizadMmM3XqVLNjxw5z6NAhs3LlSnPzzTebG264wfF4oY8++sjMnz/f7N271xw8eNDMnz/fhIWFmb59+1JLKarleq61w4cPm3Llyplhw4aZpKQks3TpUhMUFGReeuklR58tW7YYd3d3M378eLN//34THx9vypYtaz766CNHn4ULFxoPDw/z3nvvmf379zseb/Tdd985+rzxxhvGz8/PLFiwwOzfv9+MHj3aeHl5OT026/HHHzeVK1c2y5cvNz/++KMZOHCgCQoKMidPnnT0ueuuu0yDBg3Mhg0bzA8//GDuvPNOU79+fcdTDXJyckyzZs1M27Ztzfbt201iYqKJjIw0t912m2MfZ86cMVWqVDH33nuv2bNnj1m7dq2pXbu2efjhh//15+aS+++/30RGRuZph7MzZ86YHTt2mB07dhhJjrnVv/zyizHGmGeeecb069fP0f/So8BGjhxp9u3bZ6ZNm8ajwK4D4Rb5mjp1qqlatarx9PQ0rVq1Mps2bXJsa9eunenfv79T/08++cTUqVPHeHp6mgYNGpgvv/yymCsufa7lHD/77LOmVq1axsvLy5QvX95ERUWZefPmObafO3fO3H333SYsLMx4enqa0NBQ061bN6cPK33//femQ4cOJjAw0NjtdlO9enXz3//+1/z666+OPvPmzTPNmjUzvr6+xsfHx9SvX99MmDDBnDt3jlpKUS1/d60/zxs3bjSRkZHGbrebmjVrmvHjxzvNMzXmzw/G3XjjjcZut5uIiAjz3nvv5Rl35syZjnPSuHFjs3jx4jx9Jk6caKpUqWLKli1roqKinAKeMcZkZ2ebJ5980gQFBZly5cqZ6Ohoxz8GLjl16pR56KGHTEBAgAkMDDR33323OXz4sFOfo0ePmnvuucf4+vqa4OBgM2DAgDyP/dq3b5+Jjo423t7epkqVKmbEiBF55jz+W89Nenq68fb2vuyxwNnq1auNpDzLpZ+z/v37m3bt2uV5TZMmTYynp6epWbOmmT17drHXbRU2Y4xx5Z1jAAAAoLAw5xYAAACWQbgFAACAZRBuAQAAYBmEWwAAAFgG4RYAAACWQbgFAACAZRBuAQAAYBmEWwAAAFgG4RYAAACWQbgFgFIkISFBbm5u6tKli6tLAYASia/fBYBS5OGHH5avr69mzpyppKQkhYWFubokAChRuHMLAKVERkaG5s+fryFDhqhLly6aM2eO0/YlS5aodu3a8vLyUocOHfTBBx/IZrMpPT3d0Wf9+vW65ZZb5O3trfDwcD322GPKzMws3gMBgCJEuAWAUuKTTz5RRESE6tatq/vvv1+zZs3SpT++JScn695771X37t21a9cuPfLII3r22WedXn/w4EF16tRJPXr00Pfff6/58+dr/fr1GjZsmCsOBwCKBNMSAKCUaN26tXr27KnHH39cFy9eVGhoqBYsWKD27dvrmWee0ZdffqkffvjB0X/06NEaP368/vjjDwUEBOjhhx+Wm5ub3n33XUef9evXq127dsrMzJSXl5crDgsAChV3bgGgFEhKStKWLVvUp08fSZK7u7t69eqlmTNnOra3bNnS6TWtWrVyWt+1a5fmzJkjX19fxxITE6Pc3FwlJycXz4EAQBFzd3UBAIB/NnPmTF28eNHpA2TGGNntdr399ttXtY+MjAw98sgjeuyxx/Jsq1q1aqHVCgCuRLgFgBLu4sWL+vDDD/Xaa6/p9ttvd9rWvXt3ffzxx6pbt66++uorp21bt251Wm/WrJn27t2rWrVqFXnNAOAqzLkFgBJu8eLF6tWrl9LS0uTv7++0bdSoUVq1apU++eQT1a1bV0888YQGDhyonTt36sknn9Svv/6q9PR0+fv76/vvv9dNN92khx56SA8//LB8fHy0d+9erVix4qrv/gJAScecWwAo4WbOnKno6Og8wVaSevToocTERJ05c0affvqpFi5cqEaNGmn69OmOpyXY7XZJUqNGjbR27Vr99NNPuuWWW9S0aVONHTuWZ+UCsBTu3AKARY0fP14zZszQkSNHXF0KABQb5twCgEW88847atmypSpUqKANGzbolVde4Rm2AP51CLcAYBH79+/XSy+9pJMnT6pq1ap68sknFRcX5+qyAKBYMS0BAAAAlsEHygAAAGAZhFsAAABYBuEWAAAAlkG4BQAAgGUQbgEAAGAZhFsAAABYBuEWAAAAlkG4BQAAgGX8f/bF1vUKJqWtAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**6. Pairplot: Systolic vs. Diastolic across Stages**"
      ],
      "metadata": {
        "id": "Pdnwh2MGRwS3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sns.pairplot(\n",
        "    data[['Systolic_num','Diastolic_num','Stages']],\n",
        "    hue=\"Stages\",\n",
        "    diag_kind=\"kde\",\n",
        "    palette=\"husl\"\n",
        ")\n",
        "\n",
        "plt.suptitle(\"Pairplot: Systolic vs Diastolic across Stages\", y=1.02)\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 425
        },
        "id": "WC42GgTbROGN",
        "outputId": "a305a483-4728-45db-eb62-f1bbedd2272a"
      },
      "execution_count": 205,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 558.486x500 with 6 Axes>"
            ],
            "image/png": "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jpXax8bGRrRu3Vp6X/ydetyT310hhPD39xcNGjSQ3m/duvWp68rIyCj1+9KqVSvh6Ogobt26JbWdPn1aGBkZieDg4BLbdOXKFamtS5cuGt+NNWvWCABi8eLFJdbztJ+Jtm198803haWlpbh//74Qovw/85CQEAFAhIWFafQp7/fv888/FwBERkZGqfUOGDBANG/evMxt0iY1NVU4ODgIAKJp06birbfeEuvXrxd3794t0TcgIEC4uLiUaH/48KEoKCjQaLtz545QqVQa398ff/xRABDR0dFSW1FRkejevXuJ3y09evQQHh4e0mctxKPPtEOHDqJRo0ZSW3nGPz2beNjoGePn5wcHBwc4Oztj2LBhsLKywtatW1GvXj0AkM4pAIA7d+4gKysLnTt3Lveu/wkTJmjsiXhc8V+/xSZPngzg0Qmrpdm9eze8vb3RqVMnqc3KygpvvPEGrl69ij///POpNXXt2hVCiHKdEDtv3jysX78erVu3xp49ezBr1ix4eXmhTZs2GocG/Pz8ULduXXz//fdS29mzZ3HmzBm8/vrrUputrS3OnTuHv//++6nrftLu3bthbGyMKVOmaLS/++67EELg559/LveyTp48iStXrmDatGmwtbXVmPa0S46DgoLw4MEDae8E8Ojk07t37yIoKEhqs7W1xe+//45///233HWVl5WV1VOvOnr8u5uVlYXMzEx06dIFly9fRlZWllQjAOzcuRMPHjyoUA03b97EqVOnMHr0aI29ci1btkTPnj3L/B5r8+OPP8Le3l4aB4972s/k8W3NyclBZmYmOnfuLB0iBSr+M584caLG+/J+/4qXvX37dqjVaq312tra4p9//sGxY8fK3K4nqVQqnD59Gm+99Rbu3LmDlStXYsSIEXB0dMSCBQueevgUAIyNjaVzY9RqNW7fvo2HDx+ibdu2Gr/X4uLiYGpqqrF3z8jIqMTvrdu3b+PAgQN47bXXpM8+MzMTt27dgr+/P/7++2/cuHFD2m5dxz8ZFsPLM2b58uXYt28fDh48iD///BOXL1+WdvsDj36pt2/fHubm5qhVq5a0G734l//T1K9fv9RpjRo10njv5uYGIyMjjXthPOnatWto0qRJifZmzZpJ0/Vt+PDh+PXXX3Hnzh3s3bsXI0aMwMmTJxEYGCido2NkZISRI0di27ZtyM/PBwB8//33MDc3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REREJCuVejzAsWPHcPDgQaSnp0OtVmtMW7x4caUKIyIiItJG5/CycOFCzJ49G02aNIFKpYJCoZCmPf7/RERERPqkc3j54osvsGbNGowePVqP5RARERGVTedzXoyMjNCxY0d91kJERET0VDqHl+nTp2P58uX6rIWIiIjoqXQ+bDRjxgwEBATAzc0N7u7uMDU11Zi+ZcuWShdHRERE9CSdw8uUKVNw8OBBdOvWDbVr1+ZJukRERFQtdA4v69atw48//oiAgAB91kNERERUJp3PealVqxbc3Nz0WQsRERHRU+kcXubOnYvIyEjk5+frsx4iIiKiMul82GjJkiW4dOkSVCoVXF1dS5ywm5SUVOniiIiIiJ6kc3gZOHCgHssgIiIiKh+FEEIYuojqlJ2dDRsbG2RlZcHa2trQ5RC9MDj2iEhf+FRpIiIikhWdDxsZGRmVeW+XoqIiXRdNREREVCqdw8vWrVs13j948AAnT57EunXrMG/evEoXRkRERKSN3s95Wb9+PWJjY7F9+3Z9LlZveNydyDA49ohIX/R+zkv79u0RHx+v78USERERAdBzeLl37x6WLFmCevXq6XOxRERERBKdz3mxs7PTOGFXCIGcnBxYWlriu+++00txRERERE/SObxER0drvDcyMoKDgwN8fHxgZ2dXoWUtX74cn3zyCVJTU+Hp6YmlS5fC29u71P53797FrFmzsGXLFty+fRsuLi6Ijo5G3759ddkUIiIikhGdw0tISIheCoiNjUVoaChWrlwJHx8fREdHw9/fHxcuXICjo2OJ/oWFhejZsyccHR2xefNm1KtXD9euXYOtra1e6iEiIqJnW6WuNrp79y6OHj2K9PR0qNVqjWnBwcHlWoaPjw/atWuHZcuWAQDUajWcnZ0xefJkhIWFlei/cuVKfPLJJzh//nyJ5ymVB694IDIMjj0i0hedw8tPP/2EkSNHIjc3F9bW1hrnvygUCty+ffupyygsLISlpSU2b96s8aykkJAQ3L17V+vl1n379kWtWrVgaWmJ7du3w8HBASNGjMD7778PY2Pjp66Tv0CJDINjj4j0RefDRu+++y7Gjh2LhQsXwtLSUqdlZGZmoqioCCqVSqNdpVLh/PnzWue5fPkyDhw4gJEjR2L37t24ePEi3n77bTx48ACRkZEl+hcUFKCgoEB6n52drVOtRFQxHHtEVFV0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+y67oaGhCAkJQdu2beHt7Y3o6Gjk5eVhzJgxAIDg4GDUq1cPUVFRMDc3R4sWLTTmt7W1BYAS7URERPR80jm8CCGkQzb79+9Hv379AADOzs7IzMws93KCgoKQkZGBiIgIpKamolWrVoiLi5NO4k1JSYGRkc47iIiIiOg5oxBCCF1m7N69O5ydneHn54dx48bhzz//RMOGDXHo0CGEhITg6tWrei5VP7Kzs2FjY4OsrCxYW1sbuhyiFwbHHhHpi867NKKjo5GUlIRJkyZh1qxZ0jONNm/ejA4dOuitQCIiIqLH6bznpTT379+HsbExTE1N9blYveFff0SGwbFHRPqi95u0mJub63uRRERERBKdw0tRURE+//xzbNy4ESkpKSgsLNSYfvv27UoXR0RERPSkSj1VevHixQgKCkJWVhZCQ0MxePBgGBkZYe7cuXoskYiIiOh/dA4v33//PVatWoV3330XJiYmGD58OL755htERETgv//9rz5rJCIiIpLoHF5SU1OlRwNYWVkhKysLANCvXz/s2rVLP9URERERPUHn8PLSSy/h5s2bAAA3Nzfs3bsXAHDs2DE+z4SIiIiqjM7hZdCgQdIziSZPnow5c+agUaNGCA4OxtixY/VWIBEREdHj9Hafl8TERCQmJqJRo0YaT31+1vBeE0SGwbFHRPqit/u8+Pr6an0SNBEREZE+VSi87NixA3369IGpqSl27NhRZt/+/ftXqjAiIiIibSp02MjIyAipqalwdHQs80nPCoUCRUVFeilQ37jrmsgwOPaISF8qtOdFrVZr/X8iIiKi6qLTOS9qtRpr167Fli1bcPXqVSgUCjRo0ACvvvoqRo0aBYVCoe86iYiIiADocKm0EAL9+/fH+PHjcePGDXh4eKB58+a4evUqRo8ejUGDBlVFnUREREQAdNjzsnbtWvzyyy+Ij49Ht27dNKYdOHAAAwcOxLfffovg4GC9FUlERERUrMJ7Xn744Qd88MEHJYILAHTv3h1hYWH4/vvv9VIcERER0ZMqHF7OnDmD3r17lzq9T58+OH36dKWKIiIiIipNhcPL7du3oVKpSp2uUqlw586dShVFREREVJoKh5eioiKYmJR+qoyxsTEePnxYqaKIiIiISlPhE3aFEBg9enSpT44uKCiodFFEREREpalweAkJCXlqH15pRERERFWlwuElJiamKuog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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_dkfZAMFP2IC"
      },
      "source": [
        "#**DATA SPLITTING**\n",
        "\n",
        "---\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 206,
      "metadata": {
        "id": "cQExQYHENznr",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8ca1afc0-a19f-4a83-c691-0d8e9d4eb2f8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.12/dist-packages/sklearn/impute/_base.py:635: UserWarning: Skipping features without any observed values: ['Systolic_num' 'Diastolic_num']. At least one non-missing value is needed for imputation with strategy='mean'.\n",
            "  warnings.warn(\n",
            "/usr/local/lib/python3.12/dist-packages/sklearn/impute/_base.py:635: UserWarning: Skipping features without any observed values: ['Systolic_num' 'Diastolic_num']. At least one non-missing value is needed for imputation with strategy='mean'.\n",
            "  warnings.warn(\n"
          ]
        }
      ],
      "source": [
        "#importing Train Test Split\n",
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "#seperating features and target\n",
        "X = data.drop('Stages', axis=1)\n",
        "y = data['Stages']\n",
        "\n",
        "#performing train/test split\n",
        "X_train , X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42, stratify=y)\n",
        "\n",
        "from sklearn.impute import SimpleImputer\n",
        "\n",
        "imputer = SimpleImputer(strategy='mean')\n",
        "\n",
        "X_train = imputer.fit_transform(X_train)\n",
        "X_test = imputer.transform(X_test)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 207,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Zx3ja6S3Vi3Q",
        "outputId": "7647682c-8cad-47e0-a930-0e62184a6dce"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Training samples: 1078\n",
            "Testing samples: 270\n"
          ]
        }
      ],
      "source": [
        "#Verifying Split\n",
        "print(\"Training samples:\", X_train.shape[0])\n",
        "print(\"Testing samples:\", X_test.shape[0])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QhxxIDF9XglB"
      },
      "source": [
        "# **Algorithm Implementation and Comparison**\n",
        "\n",
        "---\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 208,
      "metadata": {
        "id": "ZREG8o_aVtsK"
      },
      "outputs": [],
      "source": [
        "#importing libraries\n",
        "from sklearn.linear_model import LogisticRegression, RidgeClassifier\n",
        "from sklearn.tree import DecisionTreeClassifier\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from sklearn.svm import SVC\n",
        "from sklearn.neighbors import KNeighborsClassifier\n",
        "from sklearn.naive_bayes import GaussianNB\n",
        "\n",
        "from sklearn.metrics import accuracy_score, classification_report, confusion_matrix\n",
        "\n",
        "#accuracy dictionary\n",
        "accuracy = {}"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4D2BC460X18L"
      },
      "source": [
        "**1. Logistic Regression**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 209,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "O5SBl2d7X0cz",
        "outputId": "9ac46057-ee93-43e6-89da-77d1cf01ba36"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Logistic Regression:\n",
            "Accuracy: 0.9407407407407408\n",
            "Classification Report:\n",
            "               precision    recall  f1-score   support\n",
            "\n",
            "           0       1.00      1.00      1.00        23\n",
            "           1       1.00      1.00      1.00       120\n",
            "           2       1.00      0.80      0.89        79\n",
            "           3       0.75      1.00      0.86        48\n",
            "\n",
            "    accuracy                           0.94       270\n",
            "   macro avg       0.94      0.95      0.94       270\n",
            "weighted avg       0.96      0.94      0.94       270\n",
            "\n",
            "Confusion Matrix:\n",
            " [[ 23   0   0   0]\n",
            " [  0 120   0   0]\n",
            " [  0   0  63  16]\n",
            " [  0   0   0  48]]\n"
          ]
        }
      ],
      "source": [
        "from sklearn.impute import SimpleImputer\n",
        "from sklearn.linear_model import LogisticRegression\n",
        "from sklearn.metrics import accuracy_score, classification_report, confusion_matrix\n",
        "\n",
        "# Fix NaN values without changing dataset structure\n",
        "imputer = SimpleImputer(strategy='mean')\n",
        "\n",
        "X_train_clean = imputer.fit_transform(X_train)\n",
        "X_test_clean = imputer.transform(X_test)\n",
        "\n",
        "log_reg = LogisticRegression(max_iter=1000)\n",
        "\n",
        "log_reg.fit(X_train_clean, y_train)\n",
        "\n",
        "y_pred = log_reg.predict(X_test_clean)\n",
        "\n",
        "print(\"Logistic Regression:\")\n",
        "print(\"Accuracy:\", accuracy_score(y_test, y_pred))\n",
        "print(\"Classification Report:\\n\", classification_report(y_test, y_pred))\n",
        "print(\"Confusion Matrix:\\n\", confusion_matrix(y_test, y_pred))\n",
        "\n",
        "accuracy['Logistic Regression'] = accuracy_score(y_test, y_pred)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NmJZotT7rLkE"
      },
      "source": [
        "**2. Decision Tree**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 210,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4M9MBilFYc2K",
        "outputId": "431d8eb8-955e-4702-f8f5-2a07d96495b7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Decision Tree:\n",
            "Accuracy: 1.0\n",
            "Classification Report:\n",
            "               precision    recall  f1-score   support\n",
            "\n",
            "           0       1.00      1.00      1.00        23\n",
            "           1       1.00      1.00      1.00       120\n",
            "           2       1.00      1.00      1.00        79\n",
            "           3       1.00      1.00      1.00        48\n",
            "\n",
            "    accuracy                           1.00       270\n",
            "   macro avg       1.00      1.00      1.00       270\n",
            "weighted avg       1.00      1.00      1.00       270\n",
            "\n",
            "Confusion Matrix:\n",
            " [[ 23   0   0   0]\n",
            " [  0 120   0   0]\n",
            " [  0   0  79   0]\n",
            " [  0   0   0  48]]\n"
          ]
        }
      ],
      "source": [
        "decisionTree = DecisionTreeClassifier()\n",
        "\n",
        "decisionTree.fit(X_train, y_train)\n",
        "\n",
        "y_pred = decisionTree.predict(X_test)\n",
        "\n",
        "print(\"Decision Tree:\")\n",
        "print(\"Accuracy:\", accuracy_score(y_test, y_pred))\n",
        "print(\"Classification Report:\\n\", classification_report(y_test, y_pred))\n",
        "print(\"Confusion Matrix:\\n\", confusion_matrix(y_test, y_pred))\n",
        "\n",
        "accuracy['Decision Tree'] = accuracy_score(y_test, y_pred)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "44S1Ilx_rUzZ"
      },
      "source": [
        "**3. Random Forest**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 211,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qpTidSg_YeUs",
        "outputId": "79697ade-78de-4f8a-d0bb-0e74891d4a08"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Random Forest:\n",
            "Accuracy: 1.0\n",
            "Classification Report:\n",
            "               precision    recall  f1-score   support\n",
            "\n",
            "           0       1.00      1.00      1.00        23\n",
            "           1       1.00      1.00      1.00       120\n",
            "           2       1.00      1.00      1.00        79\n",
            "           3       1.00      1.00      1.00        48\n",
            "\n",
            "    accuracy                           1.00       270\n",
            "   macro avg       1.00      1.00      1.00       270\n",
            "weighted avg       1.00      1.00      1.00       270\n",
            "\n",
            "Confusion Matrix:\n",
            " [[ 23   0   0   0]\n",
            " [  0 120   0   0]\n",
            " [  0   0  79   0]\n",
            " [  0   0   0  48]]\n"
          ]
        }
      ],
      "source": [
        "randomforest = RandomForestClassifier()\n",
        "\n",
        "randomforest.fit(X_train, y_train)\n",
        "\n",
        "y_pred = randomforest.predict(X_test)\n",
        "\n",
        "print(\"Random Forest:\")\n",
        "print(\"Accuracy:\", accuracy_score(y_test, y_pred))\n",
        "print(\"Classification Report:\\n\", classification_report(y_test, y_pred))\n",
        "print(\"Confusion Matrix:\\n\", confusion_matrix(y_test, y_pred))\n",
        "\n",
        "accuracy['Random Forest'] = accuracy_score(y_test, y_pred)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qs9u00P_rZIt"
      },
      "source": [
        "**4. Support Vector Machine (SVM)**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 212,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "26ccbvkfYl4t",
        "outputId": "d1384f98-def4-4f8a-9f3a-a7f1eb71bcd5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "SVM:\n",
            "Accuracy: 1.0\n",
            "Classification Report:\n",
            "               precision    recall  f1-score   support\n",
            "\n",
            "           0       1.00      1.00      1.00        23\n",
            "           1       1.00      1.00      1.00       120\n",
            "           2       1.00      1.00      1.00        79\n",
            "           3       1.00      1.00      1.00        48\n",
            "\n",
            "    accuracy                           1.00       270\n",
            "   macro avg       1.00      1.00      1.00       270\n",
            "weighted avg       1.00      1.00      1.00       270\n",
            "\n",
            "Confusion Matrix:\n",
            " [[ 23   0   0   0]\n",
            " [  0 120   0   0]\n",
            " [  0   0  79   0]\n",
            " [  0   0   0  48]]\n"
          ]
        }
      ],
      "source": [
        "svm = SVC()\n",
        "\n",
        "svm.fit(X_train, y_train)\n",
        "\n",
        "y_pred = svm.predict(X_test)\n",
        "\n",
        "print(\"SVM:\")\n",
        "\n",
        "print(\"Accuracy:\", accuracy_score(y_test, y_pred))\n",
        "\n",
        "print(\"Classification Report:\\n\", classification_report(y_test, y_pred))\n",
        "\n",
        "print(\"Confusion Matrix:\\n\", confusion_matrix(y_test, y_pred))\n",
        "\n",
        "accuracy['SVM'] = accuracy_score(y_test, y_pred)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "z77mMxL7rec6"
      },
      "source": [
        "**5. K-Nearest Neighbors (KNN)**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 213,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cwrL9nwQYq7G",
        "outputId": "9cc0822b-e443-4b29-b6f8-625de5b95a36"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "KNN:\n",
            "Accuracy: 0.9703703703703703\n",
            "Classification Report:\n",
            "               precision    recall  f1-score   support\n",
            "\n",
            "           0       1.00      0.65      0.79        23\n",
            "           1       0.94      1.00      0.97       120\n",
            "           2       1.00      1.00      1.00        79\n",
            "           3       1.00      1.00      1.00        48\n",
            "\n",
            "    accuracy                           0.97       270\n",
            "   macro avg       0.98      0.91      0.94       270\n",
            "weighted avg       0.97      0.97      0.97       270\n",
            "\n",
            "Confusion Matrix:\n",
            " [[ 15   8   0   0]\n",
            " [  0 120   0   0]\n",
            " [  0   0  79   0]\n",
            " [  0   0   0  48]]\n"
          ]
        }
      ],
      "source": [
        "knn = KNeighborsClassifier(n_neighbors=5)\n",
        "\n",
        "knn.fit(X_train, y_train)\n",
        "\n",
        "y_pred = knn.predict(X_test)\n",
        "\n",
        "print(\"KNN:\")\n",
        "print(\"Accuracy:\", accuracy_score(y_test, y_pred))\n",
        "print(\"Classification Report:\\n\", classification_report(y_test, y_pred))\n",
        "print(\"Confusion Matrix:\\n\", confusion_matrix(y_test, y_pred))\n",
        "\n",
        "accuracy['KNN'] = accuracy_score(y_test, y_pred)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "uW_Vg5CkrlVC"
      },
      "source": [
        "**6. Ridge Classifier**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 214,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Xpn-R_JMYsYi",
        "outputId": "9bacc5ac-4da9-4ba8-bac6-3da8e63a8b87"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "RidgeClassifier:\n",
            "Accuracy: 0.8888888888888888\n",
            "Classification Report:\n",
            "               precision    recall  f1-score   support\n",
            "\n",
            "           0       1.00      0.39      0.56        23\n",
            "           1       0.90      1.00      0.94       120\n",
            "           2       1.00      0.80      0.89        79\n",
            "           3       0.75      1.00      0.86        48\n",
            "\n",
            "    accuracy                           0.89       270\n",
            "   macro avg       0.91      0.80      0.81       270\n",
            "weighted avg       0.91      0.89      0.88       270\n",
            "\n",
            "Confusion Matrix:\n",
            " [[  9  14   0   0]\n",
            " [  0 120   0   0]\n",
            " [  0   0  63  16]\n",
            " [  0   0   0  48]]\n"
          ]
        }
      ],
      "source": [
        "RC = RidgeClassifier()\n",
        "\n",
        "RC.fit(X_train, y_train)\n",
        "\n",
        "y_pred = RC.predict(X_test)\n",
        "\n",
        "print(\"RidgeClassifier:\")\n",
        "print(\"Accuracy:\", accuracy_score(y_test, y_pred))\n",
        "print(\"Classification Report:\\n\", classification_report(y_test, y_pred))\n",
        "print(\"Confusion Matrix:\\n\", confusion_matrix(y_test, y_pred))\n",
        "\n",
        "accuracy['RidgeClassifier'] = accuracy_score(y_test, y_pred)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1QfEL5fVrqG8"
      },
      "source": [
        "**7. Gaussian Naive Bayes (Selected Model)**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 215,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AaWLw93OY6xA",
        "outputId": "5d7b5104-cffb-4249-fb05-8fc9336d2d6a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Naive Bayes:\n",
            "Accuracy: 0.8444444444444444\n",
            "Classification Report:\n",
            "               precision    recall  f1-score   support\n",
            "\n",
            "           0       1.00      1.00      1.00        23\n",
            "           1       1.00      1.00      1.00       120\n",
            "           2       1.00      0.47      0.64        79\n",
            "           3       0.53      1.00      0.70        48\n",
            "\n",
            "    accuracy                           0.84       270\n",
            "   macro avg       0.88      0.87      0.83       270\n",
            "weighted avg       0.92      0.84      0.84       270\n",
            "\n",
            "Confusion Matrix:\n",
            " [[ 23   0   0   0]\n",
            " [  0 120   0   0]\n",
            " [  0   0  37  42]\n",
            " [  0   0   0  48]]\n"
          ]
        }
      ],
      "source": [
        "naive_bayes = GaussianNB()\n",
        "\n",
        "naive_bayes.fit(X_train, y_train)\n",
        "\n",
        "y_pred = naive_bayes.predict(X_test)\n",
        "\n",
        "print(\"Naive Bayes:\")\n",
        "print(\"Accuracy:\", accuracy_score(y_test, y_pred))\n",
        "print(\"Classification Report:\\n\", classification_report(y_test, y_pred))\n",
        "print(\"Confusion Matrix:\\n\", confusion_matrix(y_test, y_pred))\n",
        "\n",
        "accuracy['Naive Bayes'] = accuracy_score(y_test, y_pred)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "T-11M3f6rvcN"
      },
      "source": [
        "#**MODEL COMPARISION TABLE**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 216,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 269
        },
        "id": "9_oneg9iY-_1",
        "outputId": "a036d87a-a18e-4983-8b19-fd39a00b3493"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                 Model  Accuracy\n",
              "1        Decision Tree  1.000000\n",
              "2        Random Forest  1.000000\n",
              "3                  SVM  1.000000\n",
              "4                  KNN  0.970370\n",
              "0  Logistic Regression  0.940741\n",
              "5      RidgeClassifier  0.888889\n",
              "6          Naive Bayes  0.844444"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-98829448-3ab2-47b1-8558-5671851345ef\" class=\"colab-df-container\">\n",
              "    <div>\n",
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
              "      <th>Model</th>\n",
              "      <th>Accuracy</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Decision Tree</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Random Forest</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>SVM</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>KNN</td>\n",
              "      <td>0.970370</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Logistic Regression</td>\n",
              "      <td>0.940741</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>RidgeClassifier</td>\n",
              "      <td>0.888889</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>Naive Bayes</td>\n",
              "      <td>0.844444</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-98829448-3ab2-47b1-8558-5671851345ef')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-98829448-3ab2-47b1-8558-5671851345ef button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-98829448-3ab2-47b1-8558-5671851345ef');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "  <div id=\"id_6548ecf6-a2be-4394-ab8a-99ed465d1994\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('accuracy_df')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_6548ecf6-a2be-4394-ab8a-99ed465d1994 button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('accuracy_df');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "accuracy_df",
              "summary": "{\n  \"name\": \"accuracy_df\",\n  \"rows\": 7,\n  \"fields\": [\n    {\n      \"column\": \"Model\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 7,\n        \"samples\": [\n          \"Decision Tree\",\n          \"Random Forest\",\n          \"RidgeClassifier\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Accuracy\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.06174250279704269,\n        \"min\": 0.8444444444444444,\n        \"max\": 1.0,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          0.9703703703703703,\n          0.8444444444444444,\n          0.9407407407407408\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 216
        }
      ],
      "source": [
        "accuracy_df = pd.DataFrame(list(accuracy.items()), columns=['Model','Accuracy'])\n",
        "\n",
        "accuracy_df = accuracy_df.sort_values(by='Accuracy', ascending=False)\n",
        "\n",
        "accuracy_df"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 217,
      "metadata": {
        "id": "OCK4wJyqZOE8",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 341
        },
        "outputId": "4c852196-0077-4d76-dd6b-e11ec39bb5c4"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                 Model  Accuracy Generalization Assessment Selection Status\n",
              "1        Decision Tree  1.000000                Overfitted         Rejected\n",
              "2        Random Forest  1.000000                Overfitted         Rejected\n",
              "3                  SVM  1.000000                Overfitted         Rejected\n",
              "4                  KNN  0.970370                      Good       Considered\n",
              "0  Logistic Regression  0.940741                 Excellent         Selected\n",
              "5      RidgeClassifier  0.888889                      Good       Considered\n",
              "6          Naive Bayes  0.844444                      Good       Considered"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-283db668-425b-47ef-bca8-50ce86398875\" class=\"colab-df-container\">\n",
              "    <div>\n",
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
              "      <th>Model</th>\n",
              "      <th>Accuracy</th>\n",
              "      <th>Generalization Assessment</th>\n",
              "      <th>Selection Status</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Decision Tree</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>Overfitted</td>\n",
              "      <td>Rejected</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Random Forest</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>Overfitted</td>\n",
              "      <td>Rejected</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>SVM</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>Overfitted</td>\n",
              "      <td>Rejected</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>KNN</td>\n",
              "      <td>0.970370</td>\n",
              "      <td>Good</td>\n",
              "      <td>Considered</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Logistic Regression</td>\n",
              "      <td>0.940741</td>\n",
              "      <td>Excellent</td>\n",
              "      <td>Selected</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>RidgeClassifier</td>\n",
              "      <td>0.888889</td>\n",
              "      <td>Good</td>\n",
              "      <td>Considered</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>Naive Bayes</td>\n",
              "      <td>0.844444</td>\n",
              "      <td>Good</td>\n",
              "      <td>Considered</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-283db668-425b-47ef-bca8-50ce86398875')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-283db668-425b-47ef-bca8-50ce86398875 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-283db668-425b-47ef-bca8-50ce86398875');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "  <div id=\"id_adddc358-75f7-42a8-b03e-4cda0ab40f76\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('accuracy_df')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_adddc358-75f7-42a8-b03e-4cda0ab40f76 button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('accuracy_df');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "accuracy_df",
              "summary": "{\n  \"name\": \"accuracy_df\",\n  \"rows\": 7,\n  \"fields\": [\n    {\n      \"column\": \"Model\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 7,\n        \"samples\": [\n          \"Decision Tree\",\n          \"Random Forest\",\n          \"RidgeClassifier\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Accuracy\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.06174250279704269,\n        \"min\": 0.8444444444444444,\n        \"max\": 1.0,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          0.9703703703703703,\n          0.8444444444444444,\n          0.9407407407407408\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Generalization Assessment\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 3,\n        \"samples\": [\n          \"Overfitted\",\n          \"Good\",\n          \"Excellent\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Selection Status\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 3,\n        \"samples\": [\n          \"Rejected\",\n          \"Considered\",\n          \"Selected\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 217
        }
      ],
      "source": [
        "accuracy_df[\"Generalization Assessment\"] = [\n",
        "\"Overfitted\",\n",
        "\"Overfitted\",\n",
        "\"Overfitted\",\n",
        "\"Good\",\n",
        "\"Excellent\",\n",
        "\"Good\",\n",
        "\"Good\"\n",
        "]\n",
        "\n",
        "accuracy_df[\"Selection Status\"] = [\n",
        "\"Rejected\",\n",
        "\"Rejected\",\n",
        "\"Rejected\",\n",
        "\"Considered\",\n",
        "\"Selected\",\n",
        "\"Considered\",\n",
        "\"Considered\"\n",
        "]\n",
        "\n",
        "accuracy_df"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 218,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Rdf6nyxiOu5C",
        "outputId": "a3e7e4b6-bca5-47f1-dc21-4fa8ea9a5be7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Logistic Regression Training Accuracy: 0.9703153988868275\n",
            "Logistic Regression Testing Accuracy: 0.9407407407407408\n"
          ]
        }
      ],
      "source": [
        "#computing testing and taining accuracy for logistic regression\n",
        "from sklearn.metrics import accuracy_score\n",
        "\n",
        "train_pred_lr = log_reg.predict(X_train)\n",
        "test_pred_lr = log_reg.predict(X_test)\n",
        "\n",
        "train_acc_lr = accuracy_score(y_train, train_pred_lr)\n",
        "test_acc_lr = accuracy_score(y_test, test_pred_lr)\n",
        "\n",
        "print(\"Logistic Regression Training Accuracy:\", train_acc_lr)\n",
        "print(\"Logistic Regression Testing Accuracy:\", test_acc_lr)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 219,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "n_olmMj7Ou5D",
        "outputId": "ef64308c-cf39-411e-b51e-b31b5c1b135d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Decision Tree Training Accuracy: 1.0\n",
            "Decision Tree Testing Accuracy: 1.0\n"
          ]
        }
      ],
      "source": [
        "#computing testing and training accuracy for overfitted decision tree\n",
        "train_pred_dt = decisionTree.predict(X_train)\n",
        "test_pred_dt = decisionTree.predict(X_test)\n",
        "\n",
        "train_acc_dt = accuracy_score(y_train, train_pred_dt)\n",
        "test_acc_dt = accuracy_score(y_test, test_pred_dt)\n",
        "\n",
        "print(\"Decision Tree Training Accuracy:\", train_acc_dt)\n",
        "print(\"Decision Tree Testing Accuracy:\", test_acc_dt)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 220,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YbU2jts2Ou5D",
        "outputId": "431d6b52-88c1-4ec7-9055-6f359be25f71"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       1.00      1.00      1.00        23\n",
            "           1       1.00      1.00      1.00       120\n",
            "           2       1.00      0.80      0.89        79\n",
            "           3       0.75      1.00      0.86        48\n",
            "\n",
            "    accuracy                           0.94       270\n",
            "   macro avg       0.94      0.95      0.94       270\n",
            "weighted avg       0.96      0.94      0.94       270\n",
            "\n"
          ]
        }
      ],
      "source": [
        "from sklearn.metrics import classification_report\n",
        "\n",
        "print(classification_report(y_test, log_reg.predict(X_test)))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 221,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 388
        },
        "id": "kfdtbWE6Ou5E",
        "outputId": "0de8921f-2047-4a84-ba6b-3c65204f6c31"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 2 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAhsAAAHHCAYAAAAWM5p0AAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAT21JREFUeJzt3XlcFPX/B/DXLseC3IdcKoKoCIoXHiHmSeKRiWceFd6WoClqikkemSiV94GlqZlHaWlmqSkeZCIqildq3loKCAjItSA7vz/8uV9XQMF2mIV9PXvMI/nM7Mx7dhZ48/58PjMyQRAEEBEREYlELnUAREREVLUx2SAiIiJRMdkgIiIiUTHZICIiIlEx2SAiIiJRMdkgIiIiUTHZICIiIlEx2SAiIiJRMdkgIiIiUTHZ0HNXr15Fly5dYGVlBZlMhp07d2p1/7du3YJMJsP69eu1ut/KrEOHDujQoYPUYVSYw4cPQyaT4fDhw1rZ3/r16yGTyXDr1i2t7I+AWbNmQSaTSR0GVWFMNnTA9evXMWbMGNSpUwcmJiawtLSEv78/lixZgry8PFGPHRwcjPPnz+Ozzz7Dxo0b0aJFC1GPV5GGDh0KmUwGS0vLEt/Hq1evQiaTQSaT4Ysvvij3/u/du4dZs2YhMTFRC9FWDDc3N7z55ptSh1Em8+bN03ry+7ynicvTxdDQEDVq1MDQoUPx77//inpsIn1iKHUA+u7XX39F//79oVAo8N5776FRo0YoKCjA0aNHMWXKFFy8eBFfffWVKMfOy8tDXFwcPv74Y4SGhopyjNq1ayMvLw9GRkai7P9lDA0NkZubi19++QUDBgzQWLdp0yaYmJggPz//lfZ97949zJ49G25ubmjatGmZX/f777+/0vEqq3bt2iEvLw/Gxsblet28efPQr18/BAUFabS/++67GDhwIBQKhdZinDNnDtzd3ZGfn4/jx49j/fr1OHr0KC5cuAATExOtHUdXzZgxA9OmTZM6DKrCmGxI6ObNmxg4cCBq166NgwcPwtnZWb0uJCQE165dw6+//ira8R88eAAAsLa2Fu0YMplM0h/WCoUC/v7+2LJlS7FkY/PmzejRowd+/PHHCoklNzcX1apVK/cv3cpOLpdr9TNgYGAAAwMDre0PALp166au6o0cORL29vZYsGABdu3aVexzIyZBEJCfnw9TU9MKOybwJCk3NOSvAxIPu1EkFBUVhezsbKxdu1Yj0Xiqbt26+PDDD9VfP378GJ9++ik8PDygUCjg5uaG6dOnQ6lUarzuaan86NGjaNWqFUxMTFCnTh18++236m1mzZqF2rVrAwCmTJkCmUwGNzc3AE+6H57++1kl9evu378fbdu2hbW1NczNzeHp6Ynp06er15c2ZuPgwYN4/fXXYWZmBmtra/Tq1QuXLl0q8XjXrl3D0KFDYW1tDSsrKwwbNgy5ubmlv7HPGTx4MPbs2YOMjAx128mTJ3H16lUMHjy42Pbp6emYPHkyfHx8YG5uDktLS3Tr1g1nz55Vb3P48GG0bNkSADBs2DB1Gf7peXbo0AGNGjVCQkIC2rVrh2rVqqnfl+fHbAQHB8PExKTY+QcGBsLGxgb37t0r87lqQ1k/ZyqVCrNmzYKLiwuqVauGjh074q+//oKbmxuGDh2q3q6kMRtXr15F37594eTkBBMTE9SsWRMDBw5EZmYmgCdJak5ODjZs2KB+b5/us7QxG3v27EH79u1hYWEBS0tLtGzZEps3b36l9+D1118H8KSL81mXL19Gv379YGtrCxMTE7Ro0QK7du0q9vpz586hffv2MDU1Rc2aNTF37lysW7euWNxPv1f37duHFi1awNTUFKtXrwYAZGRkYMKECahVqxYUCgXq1q2LBQsWQKVSaRxr69at8PX1VZ+3j48PlixZol5fWFiI2bNno169ejAxMYGdnR3atm2L/fv3q7cp6Xtbmz9viJjKSuiXX35BnTp10KZNmzJtP3LkSGzYsAH9+vXDpEmTEB8fj8jISFy6dAk7duzQ2PbatWvo168fRowYgeDgYHzzzTcYOnQofH190bBhQ/Tp0wfW1taYOHEiBg0ahO7du8Pc3Lxc8V+8eBFvvvkmGjdujDlz5kChUODatWv4888/X/i6AwcOoFu3bqhTpw5mzZqFvLw8LFu2DP7+/jh9+nSxRGfAgAFwd3dHZGQkTp8+jTVr1sDBwQELFiwoU5x9+vTB+++/j59++gnDhw8H8KSq0aBBAzRv3rzY9jdu3MDOnTvRv39/uLu7Izk5GatXr0b79u3x119/wcXFBV5eXpgzZw4++eQTjB49Wv3L6dlrmZaWhm7dumHgwIF455134OjoWGJ8S5YswcGDBxEcHIy4uDgYGBhg9erV+P3337Fx40a4uLiU6Ty1payfs/DwcERFRaFnz54IDAzE2bNnERgY+NJuqYKCAgQGBkKpVGLcuHFwcnLCv//+i927dyMjIwNWVlbYuHEjRo4ciVatWmH06NEAAA8Pj1L3uX79egwfPhwNGzZEeHg4rK2tcebMGezdu7fEhPJlniYENjY26raLFy/C398fNWrUwLRp02BmZoYffvgBQUFB+PHHH9G7d28AwL///ouOHTtCJpMhPDwcZmZmWLNmTandPleuXMGgQYMwZswYjBo1Cp6ensjNzUX79u3x77//YsyYMXB1dcWxY8cQHh6O+/fvY/HixQCeJPuDBg1C586d1d8Ply5dwp9//qn+Q2XWrFmIjIxUv59ZWVk4deoUTp8+jTfeeKPU90CbP2+IIJAkMjMzBQBCr169yrR9YmKiAEAYOXKkRvvkyZMFAMLBgwfVbbVr1xYACLGxseq2lJQUQaFQCJMmTVK33bx5UwAgfP755xr7DA4OFmrXrl0shpkzZwrPfmQWLVokABAePHhQatxPj7Fu3Tp1W9OmTQUHBwchLS1N3Xb27FlBLpcL7733XrHjDR8+XGOfvXv3Fuzs7Eo95rPnYWZmJgiCIPTr10/o3LmzIAiCUFRUJDg5OQmzZ88u8T3Iz88XioqKip2HQqEQ5syZo247efJksXN7qn379gIAITo6usR17du312jbt2+fAECYO3eucOPGDcHc3FwICgp66TmWV+3atYUePXqUur6sn7OkpCTB0NCwWIyzZs0SAAjBwcHqtkOHDgkAhEOHDgmCIAhnzpwRAAjbtm17YaxmZmYa+3lq3bp1AgDh5s2bgiAIQkZGhmBhYSG0bt1ayMvL09hWpVK98BhP93XgwAHhwYMHwt27d4Xt27cL1atXFxQKhXD37l31tp07dxZ8fHyE/Px8jf23adNGqFevnrpt3LhxgkwmE86cOaNuS0tLE2xtbTXiFoT/fa/u3btXI65PP/1UMDMzE/7++2+N9mnTpgkGBgbCnTt3BEEQhA8//FCwtLQUHj9+XOo5NmnS5IXXXBCKf2+L8fOG9Bu7USSSlZUFALCwsCjT9r/99hsAICwsTKN90qRJAFBsbIe3t7f6r20AqF69Ojw9PXHjxo1Xjvl5T8d6/Pzzz8VKu6W5f/8+EhMTMXToUNja2qrbGzdujDfeeEN9ns96//33Nb5+/fXXkZaWpn4Py2Lw4ME4fPgwkpKScPDgQSQlJZX6F69CoYBc/uRbo6ioCGlpaeouotOnT5f5mAqFAsOGDSvTtl26dMGYMWMwZ84c9OnTByYmJupyekUq6+csJiYGjx8/xtixYzW2Gzdu3EuPYWVlBQDYt29fubrDSrN//348evQI06ZNKzY2pKzTOQMCAlC9enXUqlUL/fr1g5mZGXbt2oWaNWsCeNK1dvDgQQwYMACPHj1CamoqUlNTkZaWhsDAQFy9elU9e2Xv3r3w8/PTGDRsa2uLIUOGlHhsd3d3BAYGarRt27YNr7/+OmxsbNTHSk1NRUBAAIqKihAbGwvgyfdgTk6ORpfI86ytrXHx4kVcvXq1TO8FoJs/b6hyY7IhEUtLSwDAo0ePyrT97du3IZfLUbduXY12JycnWFtb4/bt2xrtrq6uxfZhY2ODhw8fvmLExb399tvw9/fHyJEj4ejoiIEDB+KHH354YeLxNE5PT89i67y8vJCamoqcnByN9ufP5Wlpuzzn0r17d1hYWOD777/Hpk2b0LJly2Lv5VMqlQqLFi1CvXr1oFAoYG9vj+rVq+PcuXPqMQVlUaNGjXINBv3iiy9ga2uLxMRELF26FA4ODi99zYMHD5CUlKResrOzy3y8kpT1c/b0/89vZ2trq9H1UBJ3d3eEhYVhzZo1sLe3R2BgIFasWFGu9/ZZT8dVNGrU6JVeDwArVqzA/v37sX37dnTv3h2pqaka3R7Xrl2DIAiIiIhA9erVNZaZM2cCAFJSUgA8eW9K+myV9nlzd3cv1nb16lXs3bu32LECAgI0jjV27FjUr18f3bp1Q82aNTF8+HDs3btXY19z5sxBRkYG6tevDx8fH0yZMgXnzp174fuhiz9vqHJjsiERS0tLuLi44MKFC+V6XVn/UitttL4gCK98jKKiIo2vTU1NERsbiwMHDuDdd9/FuXPn8Pbbb+ONN94otu1/8V/O5SmFQoE+ffpgw4YN2LFjxwv78efNm4ewsDC0a9cO3333Hfbt24f9+/ejYcOGZa7gACj3jIIzZ86of4mcP3++TK9p2bIlnJ2d1cur3C+kJGLf4OnLL7/EuXPnMH36dOTl5WH8+PFo2LAh/vnnH1GPW5pWrVohICAAffv2xa5du9CoUSMMHjxYnbw9ve6TJ0/G/v37S1xKSyZepqTPiUqlwhtvvFHqsfr27QsAcHBwQGJiInbt2oW33noLhw4dQrdu3RAcHKzeV7t27XD9+nV88803aNSoEdasWYPmzZtjzZo1L42tIn7ekH7gAFEJvfnmm/jqq68QFxcHPz+/F25bu3ZtqFQqXL16FV5eXur25ORkZGRkqGeWaIONjY3GzI2nnv9rBngyrbFz587o3LkzFi5ciHnz5uHjjz/GoUOH1H+FPX8ewJNBcc+7fPky7O3tYWZm9t9PogSDBw/GN998A7lcjoEDB5a63fbt29GxY0esXbtWoz0jIwP29vbqr7X5CzknJwfDhg2Dt7c32rRpg6ioKPTu3Vs946U0mzZt0rhhWZ06df5THGX9nD39/7Vr1zT+Mk9LSyvzX7M+Pj7w8fHBjBkzcOzYMfj7+yM6Ohpz584FUPb39+nA0QsXLrzyL/xnGRgYIDIyEh07dsTy5csxbdo09ftqZGRU4uf6WbVr18a1a9eKtZfUVhoPDw9kZ2e/9FgAYGxsjJ49e6Jnz55QqVQYO3YsVq9ejYiICPX7YWtri2HDhmHYsGHIzs5Gu3btMGvWLIwcObLUc6ionzekH1jZkNBHH30EMzMzjBw5EsnJycXWX79+XT2FrXv37gCgHoX+1MKFCwEAPXr00FpcHh4eyMzM1Ci13r9/v9gI9PT09GKvfdpP/fz0uKecnZ3RtGlTbNiwQSOhuXDhAn7//Xf1eYqhY8eO+PTTT7F8+XI4OTmVup2BgUGxv8i2bdtW7I6ST5OikhKz8po6dSru3LmDDRs2YOHChXBzc0NwcHCp7+NT/v7+CAgIUC//Ndko6+esc+fOMDQ0xKpVqzS2W758+UuPkZWVhcePH2u0+fj4QC6Xa5yvmZlZmd7bLl26wMLCApGRkcVmwrzqX9YdOnRAq1atsHjxYuTn58PBwQEdOnTA6tWrcf/+/WLbP71nDfBkynJcXJzGnWXT09OxadOmMh9/wIABiIuLw759+4qty8jIUL9/aWlpGuvkcjkaN24M4H/fg89vY25ujrp1677ws1WRP29IP7CyISEPDw9s3rwZb7/9Nry8vDTuIHrs2DFs27ZNfW+BJk2aIDg4GF999RUyMjLQvn17nDhxAhs2bEBQUBA6duyotbgGDhyIqVOnonfv3hg/fjxyc3OxatUq1K9fX2OA5Jw5cxAbG4sePXqgdu3aSElJwcqVK1GzZk20bdu21P1//vnn6NatG/z8/DBixAj11FcrKyvMmjVLa+fxPLlcjhkzZrx0uzfffBNz5szBsGHD0KZNG5w/fx6bNm0q9ovcw8MD1tbWiI6OhoWFBczMzNC6desS++Bf5ODBg1i5ciVmzpypnoq7bt06dOjQAREREYiKiirX/l7m2rVr6urBs5o1a4YePXqU6XPm6OiIDz/8EF9++SXeeustdO3aFWfPnsWePXtgb2//wqrEwYMHERoaiv79+6N+/fp4/PgxNm7cCAMDA3X3AAD4+vriwIEDWLhwIVxcXODu7o7WrVsX25+lpSUWLVqEkSNHomXLlhg8eDBsbGxw9uxZ5ObmYsOGDa/0Pk2ZMgX9+/fH+vXr8f7772PFihVo27YtfHx8MGrUKNSpUwfJycmIi4vDP//8o74Py0cffYTvvvsOb7zxBsaNG6ee+urq6or09PQyVWymTJmCXbt24c0331RPIc3JycH58+exfft23Lp1C/b29hg5ciTS09PRqVMn1KxZE7dv38ayZcvQtGlTdUXC29sbHTp0gK+vL2xtbXHq1Cls3779hXcNrsifN6QnpJwKQ0/8/fffwqhRowQ3NzfB2NhYsLCwEPz9/YVly5ZpTLMrLCwUZs+eLbi7uwtGRkZCrVq1hPDwcI1tBKH06Y3PT7ksbeqrIAjC77//LjRq1EgwNjYWPD09he+++67Y9LiYmBihV69egouLi2BsbCy4uLgIgwYN0piuV9LUV0EQhAMHDgj+/v6CqampYGlpKfTs2VP466+/NLZ5erznp9Y+P/WxNM9OfS1NaVNfJ02aJDg7OwumpqaCv7+/EBcXV+KU1Z9//lnw9vYWDA0NNc6zffv2QsOGDUs85rP7ycrKEmrXri00b95cKCws1Nhu4sSJglwuF+Li4l54DuXxdJpiScuIESMEQSj75+zx48dCRESE4OTkJJiamgqdOnUSLl26JNjZ2Qnvv/++ervnp77euHFDGD58uODh4SGYmJgItra2QseOHYUDBw5o7P/y5ctCu3btBFNTU43ptKVd/127dglt2rRRf6ZatWolbNmy5YXvx9N9nTx5sti6oqIiwcPDQ/Dw8FBPLb1+/brw3nvvCU5OToKRkZFQo0YN4c033xS2b9+u8dozZ84Ir7/+uqBQKISaNWsKkZGRwtKlSwUAQlJSksb1KG1a6qNHj4Tw8HChbt26grGxsWBvby+0adNG+OKLL4SCggJBEARh+/btQpcuXQQHBwfB2NhYcHV1FcaMGSPcv39fvZ+5c+cKrVq1EqytrQVTU1OhQYMGwmeffabehyAUn/oqCNr/eUP6TSYIHMFDRNqRkZEBGxsbzJ07Fx9//LHU4eiUCRMmYPXq1cjOztb67daJdB3HbBDRKynpSbpP+/ifvR27Pnr+vUlLS8PGjRvRtm1bJhqklzhmg4heyffff4/169erb3V/9OhRbNmyBV26dIG/v7/U4UnKz88PHTp0gJeXF5KTk7F27VpkZWUhIiJC6tCIJMFkg4heSePGjWFoaIioqChkZWWpB42WNPhU33Tv3h3bt2/HV199BZlMhubNm2Pt2rVo166d1KERSYJjNoiIiKqo2NhYfP7550hISFDfwiAoKAjAkycCz5gxA7/99htu3LgBKysrBAQEYP78+RoPgExPT8e4cePwyy+/QC6Xo2/fvliyZEm5Ht7JMRtERERVVE5ODpo0aYIVK1YUW5ebm4vTp08jIiICp0+fxk8//YQrV67grbfe0thuyJAhuHjxIvbv34/du3cjNjZW/TTmsmJlg4iISA/IZDKNykZJTp48iVatWuH27dtwdXXFpUuX4O3tjZMnT6JFixYAnjxssHv37vjnn380KiAvwsoGERFRJaFUKpGVlaWxvOxOw+WRmZkJmUymfqp3XFwcrK2t1YkG8OQpyXK5HPHx8WXeb5UcIHru7n978iVpT33nsvfpERFJwaQCfhOaNiv9jq3lMbWXPWbPnq3RNnPmTK3cfTk/Px9Tp07FoEGD1E8mT0pKKvYEakNDQ9ja2iIpKanM+66SyQYREVFVFB4ejrCwMI02hULxn/dbWFiIAQMGQBCEYs880gYmG0RERGKTaWfUgkKh0Epy8aynicbt27dx8OBBdVUDAJycnJCSkqKx/ePHj5Genv7CB1o+j2M2iIiIxCaTaWfRsqeJxtWrV3HgwAHY2dlprPfz80NGRgYSEhLUbQcPHoRKpSrxwYilYWWDiIhIbFqqbJRXdnY2rl27pv765s2bSExMhK2tLZydndGvXz+cPn0au3fvRlFRkXochq2tLYyNjeHl5YWuXbti1KhRiI6ORmFhIUJDQzFw4MAyz0QBqujUVw4Q1R0cIEpEuq5CBoi2mKiV/eSdWlSu7Q8fPoyOHTsWaw8ODsasWbPg7u5e4usOHTqkfsZReno6QkNDNW7qtXTp0nLd1IuVDSIiIrGJ0AVSFh06dMCLagplqTfY2tpi8+bN/ykOJhtERERik6gbRVfo99kTERGR6FjZICIiEptE3Si6gskGERGR2NiNQkRERCQeVjaIiIjExm4UIiIiEhW7UYiIiIjEw8oGERGR2NiNQkRERKLS824UJhtERERi0/PKhn6nWkRERCQ6VjaIiIjExm4UIiIiEpWeJxv6ffZEREQkOlY2iIiIxCbX7wGiTDaIiIjExm4UIiIiIvGwskFERCQ2Pb/PBpMNIiIisbEbhYiIiEg8rGwQERGJjd0oREREJCo970ZhskFERCQ2Pa9s6HeqRURERKJjZYOIiEhs7EYhIiIiUbEbhYiIiEg8rGwQERGJjd0oREREJCp2oxARERGJh5UNIiIisbEbhYiIiESl58mGfp89ERERiY6VDQnt2PwN4o8ewr93b8FYoYCnd2MMGTUeNWq5qbdZvegznD8dj/S0VJiYmsLTuwneGTUONVzdpQtcz2zdvAkb1q1FauoD1PdsgGnTI+DTuLHUYeklXgvdwWtRThwgSlK5eO40Anv1x7xl6xGxYCUeP36MuVNDkJ+Xp96mTj0vjJ0yC4u/2Y4Z85dDgIBPp4agqKhIwsj1x949v+GLqEiMGRuCrdt2wNOzAT4YMwJpaWlSh6Z3eC10B6/FK5DJtbNUUjJBEASpg9C2c3ezpQ7hlWRmPMTIfgGYvfBreDduXuI2t29cxeTRA7Hs251wcqlVwRGWX31nc6lD+E+GDOyPho18MH3GJwAAlUqFLp3bY9DgdzFi1GiJo9MvvBa6o6pdC5MKqPGbBn2llf3k7ax87y8gcTdKamoqvvnmG8TFxSEpKQkA4OTkhDZt2mDo0KGoXr26lOFVuNycJ0mSuYVlievz8/JwaO8uODjVgF11p4oMTS8VFhTg0l8XMWLUGHWbXC7Ha6+1wbmzZySMTP/wWugOXgt6FZIlGydPnkRgYCCqVauGgIAA1K9fHwCQnJyMpUuXYv78+di3bx9atGjxwv0olUoolUqNtgJlIYwVCtFiF4NKpcL6lV/As2ETuLrX1Vi37+cfsPHrpVDm58GlVm1ERK2AkZGRRJHqj4cZD1FUVAQ7OzuNdjs7O9y8eUOiqPQTr4Xu4LV4RZW4C0QbJEs2xo0bh/79+yM6Ohqy5wbOCIKA999/H+PGjUNcXNwL9xMZGYnZs2drtL0/IRwfhE3XesxiWrN0Pu7euo5PF68ttq5t525o7PsaHqanYte2jVj46TTMXfINjI0rV0JFRKS39HyAqGTJxtmzZ7F+/fpiiQYAyGQyTJw4Ec2aNXvpfsLDwxEWFqbR9ndKodbirAhrli3A6fijmL3wa9hVdyy23szcAmbmFnCu6Yp6Xj4Y1rsDThw9hLadulZ8sHrExtoGBgYGxQa9paWlwd7eXqKo9BOvhe7gtaBXIVldx8nJCSdOnCh1/YkTJ+DoWPwX7/MUCgUsLS01lsrShSIIAtYsW4ATRw9h5ufRcHSuUZYXQRAEFBYWiB+gnjMyNoaXd0PEH/9fdU2lUiE+Pg6Nm7w8ESbt4bXQHbwWr0Ymk2llqawkq2xMnjwZo0ePRkJCAjp37qxOLJKTkxETE4Ovv/4aX3zxhVThVYg1S+fj6MG9+GjOQphUq4aH6akAgGpm5lAoTJB87x8cO/w7Grfwg6WVNdJTU7Bj63oYG5ugeau2EkevH94NHoaI6VPRsGEjNPJpjO82bkBeXh6CeveROjS9w2uhO3gtyq8yJwraIFmyERISAnt7eyxatAgrV65U3zfCwMAAvr6+WL9+PQYMGCBVeBXi91+2AwBmTdKcyjR2ykx0DHwLRsYKXLqQiF9/2oLs7CxY29jBy6cZ5i79BlY2tlKErHe6duuOh+npWLl8KVJTH8CzgRdWrl4DO5aLKxyvhe7gtaDy0on7bBQWFiI19clf9fb29v95pkVlvc9GVVTZ77NBRFVfRdxnw6z/Oq3sJ2fbMK3sp6LpxO3KjYyM4OzsLHUYREREotD3bhT9nvhLREREotOJygYREVFVpu+VDSYbREREImOyQURERKLS92SDYzaIiIiqqNjYWPTs2RMuLi6QyWTYuXOnxnpBEPDJJ5/A2dkZpqamCAgIwNWrVzW2SU9Px5AhQ2BpaQlra2uMGDEC2dnlm/XJZIOIiEhsMi0t5ZSTk4MmTZpgxYoVJa6PiorC0qVLER0djfj4eJiZmSEwMBD5+fnqbYYMGYKLFy9i//792L17N2JjYzF6dPkeda8T99nQNt5nQ3fwPhtEpOsq4j4b1kO+08p+Mja988qvlclk2LFjB4KCggA8qWq4uLhg0qRJmDx5MgAgMzMTjo6OWL9+PQYOHIhLly7B29sbJ0+eVD+Ffe/evejevTv++ecfuLi4lOnYrGwQERHpoZs3byIpKQkBAQHqNisrK7Ru3Vr9xPW4uDhYW1urEw0ACAgIgFwuR3x8fJmPxQGiREREItPWAFGlUgmlUqnRplAooHiFB5AmJSUBQLGHnjo6OqrXJSUlwcHBQWO9oaEhbG1t1duUBSsbREREItPWU18jIyNhZWWlsURGRkp9ei/FygYREVElER4ejrCwMI22V6lqAICTkxOAJ09bf/aRIcnJyWjatKl6m5SUFI3XPX78GOnp6erXlwUrG0RERCLTVmVDoVDA0tJSY3nVZMPd3R1OTk6IiYlRt2VlZSE+Ph5+fn4AAD8/P2RkZCAhIUG9zcGDB6FSqdC6desyH4uVDSIiIrFJdE+v7OxsXLt2Tf31zZs3kZiYCFtbW7i6umLChAmYO3cu6tWrB3d3d0RERMDFxUU9Y8XLywtdu3bFqFGjEB0djcLCQoSGhmLgwIFlnokCMNkgIiKqsk6dOoWOHTuqv37aBRMcHIz169fjo48+Qk5ODkaPHo2MjAy0bdsWe/fuhYmJifo1mzZtQmhoKDp37gy5XI6+ffti6dKl5YqD99kgUfE+G0Sk6yriPhv2Q7dqZT+p6wdqZT8VjZUNIiIiken7s1GYbBAREYlM35MNzkYhIiIiUbGyQUREJDb9Lmww2SAiIhIbu1GIiIiIRMTKBhERkcj0vbLBZIOIiEhk+p5ssBuFiIiIRMXKBhERkcj0vbLBZIOIiEhs+p1rsBuFiIiIxMXKBhERkcjYjUJERESiYrJBREREotL3ZINjNoiIiEhUrGwQERGJTb8LG0w2iIiIxMZuFCIiIiIRsbJBREQkMn2vbDDZICIiEpm+JxvsRiEiIiJRsbJBREQkMn2vbDDZICIiEpt+5xrsRiEiIiJxVcnKRn1nc6lDoP9n0zJU6hDoGQ9PLpc6BCK9xG4UIiIiEhWTDSIiIhKVnucaHLNBRERE4mJlg4iISGTsRiEiIiJR6XmuwW4UIiIiEhcrG0RERCJjNwoRERGJSs9zDXajEBERkbhY2SAiIhKZXK7fpQ0mG0RERCJjNwoRERGRiFjZICIiEhlnoxAREZGo9DzXYLJBREQkNn2vbHDMBhEREYmKlQ0iIiKR6Xtlg8kGERGRyPQ812A3ChEREYmLlQ0iIiKRsRuFiIiIRKXnuQa7UYiIiEhcrGwQERGJjN0oREREJCo9zzXYjUJERETiYrJBREQkMplMppWlPIqKihAREQF3d3eYmprCw8MDn376KQRBUG8jCAI++eQTODs7w9TUFAEBAbh69aq2T5/JBhERkdhkMu0s5bFgwQKsWrUKy5cvx6VLl7BgwQJERUVh2bJl6m2ioqKwdOlSREdHIz4+HmZmZggMDER+fr5Wz59jNoiIiEQmxQDRY8eOoVevXujRowcAwM3NDVu2bMGJEycAPKlqLF68GDNmzECvXr0AAN9++y0cHR2xc+dODBw4UGuxsLJBRERUSSiVSmRlZWksSqWyxG3btGmDmJgY/P333wCAs2fP4ujRo+jWrRsA4ObNm0hKSkJAQID6NVZWVmjdujXi4uK0GjeTDSIiIpFpqxslMjISVlZWGktkZGSJx5w2bRoGDhyIBg0awMjICM2aNcOECRMwZMgQAEBSUhIAwNHRUeN1jo6O6nXawm4UIiIikWmrGyU8PBxhYWEabQqFosRtf/jhB2zatAmbN29Gw4YNkZiYiAkTJsDFxQXBwcFaiaesmGwQERFVEgqFotTk4nlTpkxRVzcAwMfHB7dv30ZkZCSCg4Ph5OQEAEhOToazs7P6dcnJyWjatKlW42Y3ChERkcikmI2Sm5sLuVzz17yBgQFUKhUAwN3dHU5OToiJiVGvz8rKQnx8PPz8/P7zOT+LlQ0iIiKRSTEbpWfPnvjss8/g6uqKhg0b4syZM1i4cCGGDx+ujmnChAmYO3cu6tWrB3d3d0RERMDFxQVBQUFajYXJBhERURW0bNkyREREYOzYsUhJSYGLiwvGjBmDTz75RL3NRx99hJycHIwePRoZGRlo27Yt9u7dCxMTE63GIhOevZVYFZH/WOoI6CmblqFSh0DPeHhyudQhEOkckwr4s7vtF39oZT9HJ7+ulf1UNFY2iIiIRKbvT33lAFEiIiISFSsbREREImNlg3TO1s2b0O2NTmjZzAdDBvbH+XPnpA6pyvFv7oHti8fgxu+fIe/McvTs0Fi9ztBQjrnje+HkD9OReuxL3Pj9M6z59F04V7fS2IeNZTWs+ywYyX98jvuxUVg1czDMTI0r+lT0Cr83dAevRflIMfVVlzDZ0DF79/yGL6IiMWZsCLZu2wFPzwb4YMwIpKWlSR1alWJmqsD5v//FhMjvi62rZmKMpl61MP/rPfAbtAADJ32N+rUdsW3xGI3t1s0LhpeHM978YDn6jo9G2+Z1sSJicEWdgt7h94bu4LUoPykeMa9LmGzomI0b1qFPvwEI6t0XHnXrYsbM2TAxMcHOn36UOrQq5fc//8Lslbux61Dxv8aysvPx5gfL8eP+M7h6OwUnzt/CxPk/wNfbFbWcbAAAnu6OCPRviLFzNuPkhds4lngDYQu2oX9g82IVENIOfm/oDl4LKi8mGzqksKAAl/66iNf82qjb5HI5XnutDc6dPSNhZGRpYQqVSoWMR3kAgNaN3fEwKxen/7qj3uZg/BWoVAJaNqotVZhVFr83dAevxathN4oOu3v3rvpOZ/rgYcZDFBUVwc7OTqPdzs4OqampEkVFCmNDzB3fCz/sTcCjnHwAgKOdJR6kP9LYrqhIhfSsXDjaW0oRZpXG7w3dwWvxatiNosPS09OxYcOGF26jVCqRlZWlsSiVygqKkKo6Q0M5vosaAZlMhvHzio/vICKil5N06uuuXbteuP7GjRsv3UdkZCRmz56t0fZxxEzM+GTWfwlNEjbWNjAwMCg2yCotLQ329vYSRaW/DA3l2LRgBFydbdBt9DJ1VQMAktOyUN3WQmN7AwM5bC2rITk1q6JDrfL4vaE7eC1eTSUuSmiFpMlGUFAQZDIZXnTH9JeVjcLDwxEWFqbRJhiU7fG7usbI2Bhe3g0RfzwOnToHAABUKhXi4+MwcNA7EkenX54mGh6u1dF19FKkZ+ZorI8/dxM2ltXQzKsWzly6CwDo0LI+5HIZTl64LUXIVRq/N3QHr8Wrket5tiFpsuHs7IyVK1eiV69eJa5PTEyEr6/vC/ehUCigUGgmF5X52SjvBg9DxPSpaNiwERr5NMZ3GzcgLy8PQb37SB1alWJmagyPWtXVX7vVsEPj+jXwMCsX91MzsfnzkWjWoBb6fBgNA7kMjnZPqhjpmbkofFyEKzeTse/Pi1gRMRjjP9sKI0MDLJo2ANv2ncb9B5lSnVaVxu8N3cFrQeUlabLh6+uLhISEUpONl1U9qqKu3brjYXo6Vi5fitTUB/Bs4IWVq9fAjuVJrWruXRu/r/lQ/XXU5L4AgI27jmNu9G/qm3yd+D5c43VdRi7BHwlXAQDDpm/AomkD8NvqcVCpBOyMScSkqG0VdAb6h98buoPXovz0vLAh7VNf//jjD+Tk5KBr164lrs/JycGpU6fQvn37cu23Mlc2qho+9VW38KmvRMVVxFNfA1fGa2U/+8a21sp+KpqklY3XX3/xo3LNzMzKnWgQERHpGrmeVzZ0euorERERVX586isREZHIKvMNubSByQYREZHI9DzXYDcKERERiYuVDSIiIpHJoN+lDSYbREREIuNsFCIiIiIRsbJBREQkMs5GISIiIlHpea7BbhQiIiISFysbREREIuMj5omIiEhUep5rMNkgIiISm74PEOWYDSIiIhIVKxtEREQi0/PCBpMNIiIisen7AFF2oxAREZGoWNkgIiISmX7XNZhsEBERiY6zUYiIiIhExMoGERGRyPT9EfNlSjZ27dpV5h2+9dZbrxwMERFRVaTv3ShlSjaCgoLKtDOZTIaioqL/Eg8RERFVMWVKNlQqldhxEBERVVl6XtjgmA0iIiKxsRvlFeTk5ODIkSO4c+cOCgoKNNaNHz9eK4ERERFVFRwgWk5nzpxB9+7dkZubi5ycHNja2iI1NRXVqlWDg4MDkw0iIiLSUO77bEycOBE9e/bEw4cPYWpqiuPHj+P27dvw9fXFF198IUaMRERElZpMJtPKUlmVO9lITEzEpEmTIJfLYWBgAKVSiVq1aiEqKgrTp08XI0YiIqJKTaalpbIqd7JhZGQEufzJyxwcHHDnzh0AgJWVFe7evavd6IiIiKjSK/eYjWbNmuHkyZOoV68e2rdvj08++QSpqanYuHEjGjVqJEaMRERElRofMV9O8+bNg7OzMwDgs88+g42NDT744AM8ePAAX331ldYDJCIiquxkMu0slVW5KxstWrRQ/9vBwQF79+7VakBERERUtfCmXkRERCKrzDNJtKHcyYa7u/sL37QbN278p4CIiIiqGj3PNcqfbEyYMEHj68LCQpw5cwZ79+7FlClTtBUXERERVRHlTjY+/PDDEttXrFiBU6dO/eeAiIiIqhqpZqP8+++/mDp1Kvbs2YPc3FzUrVsX69atU4+/FAQBM2fOxNdff42MjAz4+/tj1apVqFevnlbjKPdslNJ069YNP/74o7Z2R0REVGVIMRvl4cOH8Pf3h5GREfbs2YO//voLX375JWxsbNTbREVFYenSpYiOjkZ8fDzMzMwQGBiI/Px8rZ6/1gaIbt++Hba2ttraHRERUZUhxQDRBQsWoFatWli3bp26zd3dXf1vQRCwePFizJgxA7169QIAfPvtt3B0dMTOnTsxcOBArcXySjf1evZNEwQBSUlJePDgAVauXKm1wIiIiEiTUqmEUqnUaFMoFFAoFMW23bVrFwIDA9G/f38cOXIENWrUwNixYzFq1CgAwM2bN5GUlISAgAD1a6ysrNC6dWvExcVJm2z06tVLI9mQy+WoXr06OnTogAYNGmgtMKoaHp5cLnUI9IzQHy9IHQL9v/BOHlKHQP/Po7qp6MfQ1piFyMhIzJ49W6Nt5syZmDVrVrFtb9y4gVWrViEsLAzTp0/HyZMnMX78eBgbGyM4OBhJSUkAAEdHR43XOTo6qtdpS7mTjZJOiIiIiEqnrW6U8PBwhIWFabSVVNUAAJVKhRYtWmDevHkAnvRMXLhwAdHR0QgODtZKPGVV7mTLwMAAKSkpxdrT0tJgYGCglaCIiIioOIVCAUtLS42ltGTD2dkZ3t7eGm1eXl7qB6g6OTkBAJKTkzW2SU5OVq/TlnInG4IglNiuVCphbGz8nwMiIiKqauQy7Szl4e/vjytXrmi0/f3336hduzaAJ4NFnZycEBMTo16flZWF+Ph4+Pn5/edzflaZu1GWLl0K4EkpaM2aNTA3N1evKyoqQmxsLMdsEBERlaC8iYI2TJw4EW3atMG8efMwYMAAnDhxAl999ZX6oakymQwTJkzA3LlzUa9ePbi7uyMiIgIuLi4ICgrSaixlTjYWLVoE4EllIzo6WqPLxNjYGG5uboiOjtZqcERERPRqWrZsiR07diA8PBxz5syBu7s7Fi9ejCFDhqi3+eijj5CTk4PRo0cjIyMDbdu2xd69e2FiYqLVWGRCaf0ipejYsSN++uknjZuC6Jr8x1JHQKSbOBtFd3A2iu6oiNkok3658vKNyuDLnp5a2U9FK/dslEOHDokRBxERUZUlRTeKLin3ANG+fftiwYIFxdqjoqLQv39/rQRFREREVUe5k43Y2Fh07969WHu3bt0QGxurlaCIiIiqEimejaJLyt2Nkp2dXeIUVyMjI2RlZWklKCIioqpEqqe+6opyVzZ8fHzw/fffF2vfunVrsZuHEBER0ZNfttpYKqtyVzYiIiLQp08fXL9+HZ06dQIAxMTEYPPmzdi+fbvWAyQiIqLKrdzJRs+ePbFz507MmzcP27dvh6mpKZo0aYKDBw/yEfNEREQl0PNelPInGwDQo0cP9OjRA8CTW5tu2bIFkydPRkJCAoqKirQaIBERUWXHMRuvKDY2FsHBwXBxccGXX36JTp064fjx49qMjYiIiKqAclU2kpKSsH79eqxduxZZWVkYMGAAlEoldu7cycGhREREpdDzwkbZKxs9e/aEp6cnzp07h8WLF+PevXtYtmyZmLERERFVCVI89VWXlLmysWfPHowfPx4ffPAB6tWrJ2ZMREREVIWUubJx9OhRPHr0CL6+vmjdujWWL1+O1NRUMWMjIiKqEuQymVaWyqrMycZrr72Gr7/+Gvfv38eYMWOwdetWuLi4QKVSYf/+/Xj06JGYcRIREVVa+n678nLPRjEzM8Pw4cNx9OhRnD9/HpMmTcL8+fPh4OCAt956S4wYiYiIqBL7T3c/9fT0RFRUFP755x9s2bJFWzERERFVKRwgqgUGBgYICgpCUFCQNnZHRERUpchQiTMFLdBKskFERESlq8xVCW2ozA+RIyIiokqAlQ0iIiKR6Xtlg8kGERGRyGSVed6qFrAbhYiIiETFygYREZHI2I1CREREotLzXhR2oxAREZG4WNkgIiISWWV+iJo2MNkgIiISmb6P2WA3ChEREYmKlQ0iIiKR6XkvCpMNIiIiscn5IDYiIiISk75XNjhmg4iIiETFygYREZHI9H02CpMNHbR18yZsWLcWqakPUN+zAaZNj4BP48ZSh6W3eD0qnrWpIfo1dkIjZ3MYG8iRkl2AdSf+we2H+QCAtxo6oKWrFWyrGeGxSsDt9DzsOJ+Mm+l5Ekde9ZxPTMCPmzfg2pVLSE97gBnzFqJNu04a29y5dQPrVi3B+cQEFBU9hqtbHXw890s4ODlLFLXu0ff7bLAbRcfs3fMbvoiKxJixIdi6bQc8PRvggzEjkJaWJnVoeonXo+JVM5JjWuc6KBIELIm9jU/2XsUPiUnILVCpt0l6pMTm0/cwc+9VLIi5gbTcAkxs7wZzhYGEkVdN+Xl5cK9bH2PDwktcf//fu5gydhhq1nbDgmVrsHLDNgwaOhrGCkUFR0q6jJUNHbNxwzr06TcAQb37AgBmzJyN2NjD2PnTjxgxarTE0ekfXo+K182rOtJzC7HuxL/qttScQo1tTtzJ1Pj6+zNJeL2OLWpameBySk6FxKkvWvq1RUu/tqWu3/DVcrTwa4sRYyeq25xr1KqI0CoVPS9ssLKhSwoLCnDpr4t4za+Nuk0ul+O119rg3NkzEkamn3g9pNHExQK30/PwfptaWNirAT7p4oHX69iUur2BXIZ2HjbILSjCPxn5FRgpqVQqnDz2B2rUqo0ZYR9g0JsdMWHUOzgWe1Dq0HSOXCbTylJZMdnQIQ8zHqKoqAh2dnYa7XZ2dkhNTZUoKv3F6yGN6ubG6FDXFsmPCrDoyC0cvpaOQc2c0cbNWmO7xs4WWN7HC6v6eeON+vZYeOQWsguKpAlaT2U8TEdeXi62ffcNfFu3wdxFq9CmXSd89vEknD9zSurwSIdI3o2Sl5eHhIQE2NrawtvbW2Ndfn4+fvjhB7z33nulvl6pVEKpVGq0CQYKKNhfSFQpyQDcepiPHeeTAQB3M/JRw8oE7T1scexWhnq7yynZmPP7dZgrDPB6HVuM8auFeQeu45GSCUdFEYQn42hea9sBvd9+FwDgUa8BLl04i992bodPsxZShqdTKnFRQiskrWz8/fff8PLyQrt27eDj44P27dvj/v376vWZmZkYNmzYC/cRGRkJKysrjeXzBZFihy4KG2sbGBgYFBt8mJaWBnt7e4mi0l+8HtLIzH+M+1ma3SH3s5SwrWak0VZQJCAluwA30vKw4eS/UAkC2r6gu4W0z9LKBgYGhnB189Bor1XbHSkp90t5lX6Sa2mprCSNferUqWjUqBFSUlJw5coVWFhYwN/fH3fu3CnzPsLDw5GZmamxTJla8qhpXWdkbAwv74aIPx6nblOpVIiPj0PjJs0kjEw/8XpI41pqLhwtNCuTjhbGSMstLOUVT8hkMhjJK/OP48rHyMgI9b288c/dWxrt/969DQdHTnul/5G0G+XYsWM4cOAA7O3tYW9vj19++QVjx47F66+/jkOHDsHMzOyl+1AoineZ5D8WK2LxvRs8DBHTp6Jhw0Zo5NMY323cgLy8PAT17iN1aHqJ16Pi7f87DdM610F3r+o4dTcTbramaOdhi29PPZmdYmwgQw9vB5y9l4WMvMewUBigY1072Jga4tTdzJfsncorLzcX9/793x+Ayff/xfWrl2FhYQUHJ2f0HTQU82d+BJ8mzdG4eUskxB9D/LFYLFi6RsKodY9Mz/tRJE028vLyYGj4vxBkMhlWrVqF0NBQtG/fHps3b5YwOml07dYdD9PTsXL5UqSmPoBnAy+sXL0GdizbS4LXo+LdSs/DyqN30KexI3o2rI7UnAJsPXMf8befJBIqAXC2NEYbN1eYKwyQU1CEm+l5WHDwJu5lKV+ydyqvq5cvYtr4Ueqvv172JQAgoFtPhH38Kdq074TQyTPww3drEb04CjVda+PjuV+gIat/GvQ71QBkgiAIUh28VatWGDduHN59991i60JDQ7Fp0yZkZWWhqKh8A74qc2WDSEyhP16QOgT6f+GdPF6+EVUIj+qmoh/ju4R/tLKfd3xramU/FU3SDs7evXtjy5YtJa5bvnw5Bg0aBAlzISIiItICSSsbYmFlg6hkrGzoDlY2dEdFVDY2aamyMaSSVjYkv88GERFRVafn40Mr9bRdIiIiqgRY2SAiIhIZp74SERGRqPS9G0Hfz5+IiEgvzJ8/HzKZDBMmTFC35efnIyQkBHZ2djA3N0ffvn2RnJys9WMz2SAiIhKZTCbTyvKqTp48idWrV6Nx48Ya7RMnTsQvv/yCbdu24ciRI7h37x769NH+HZKZbBAREYlMpqXlVWRnZ2PIkCH4+uuvYWPzv4cVZmZmYu3atVi4cCE6deoEX19frFu3DseOHcPx48df8WglY7JBRERUhYWEhKBHjx4ICAjQaE9ISEBhYaFGe4MGDeDq6oq4uLjnd/OfcIAoERGRyLQ1G0WpVEKp1HwGUEkPJH1q69atOH36NE6ePFlsXVJSEoyNjWFtba3R7ujoiKSkJK3E+xQrG0RERCKTa2mJjIyElZWVxhIZGVniMe/evYsPP/wQmzZtgomJiajn9zKsbBAREYlMW5WN8PBwhIWFabSVVtVISEhASkoKmjdvrm4rKipCbGwsli9fjn379qGgoAAZGRka1Y3k5GQ4OTlpJd6nmGwQERFVEi/qMnle586dcf78eY22YcOGoUGDBpg6dSpq1aoFIyMjxMTEoG/fvgCAK1eu4M6dO/Dz89Nq3Ew2iIiIRCbF/UMtLCzQqFEjjTYzMzPY2dmp20eMGIGwsDDY2trC0tIS48aNg5+fH1577TWtxsJkg4iISGS6erfyRYsWQS6Xo2/fvlAqlQgMDMTKlSu1fhw+Yp5Ij/AR87qDj5jXHRXxiPmfz2tndkcvH+2OpagorGwQERGJTC5JR4ruYLJBREQkMl3tRqkovM8GERERiYqVDSIiIpHJ2I1CREREYmI3ChEREZGIWNkgIiISGWejEBERkaj0vRuFyQYREZHI9D3Z4JgNIiIiEhUrG0RERCLj1FciIiISlVy/cw12oxAREZG4WNkgIiISGbtRiIiISFScjUJEREQkIlY2iIiIRMZuFCIiIhIVZ6MQERERiYiVDSIiIpGxG4WIiIhEpe+zUZhsEBERiUzPcw2O2SAiIiJxsbJBREQkMrme96Mw2SDSI8v7NpI6BPp/a+NvSR0C/b+Q6m6iH0O/Uw12oxAREZHIWNkgIiISm56XNphsEBERiUzf77PBbhQiIiISFSsbREREItPzyShMNoiIiMSm57kGu1GIiIhIXKxsEBERiU3PSxtMNoiIiESm77NRmGwQERGJTN8HiHLMBhEREYmKlQ0iIiKR6Xlhg8kGERGR6PQ822A3ChEREYmKlQ0iIiKRcTYKERERiYqzUYiIiIhExMoGERGRyPS8sMFkg4iISHR6nm2wG4WIiIhExcoGERGRyDgbhYiIiESl77NRmGwQERGJTM9zDY7ZICIiInGxskFERCQ2PS9tMNkgIiISmb4PEGU3ChERURUUGRmJli1bwsLCAg4ODggKCsKVK1c0tsnPz0dISAjs7Oxgbm6Ovn37Ijk5WeuxMNkgIiISmUymnaU8jhw5gpCQEBw/fhz79+9HYWEhunTpgpycHPU2EydOxC+//IJt27bhyJEjuHfvHvr06aPlswdkgiAIWt+rxPIfSx0BEdGLrY2/JXUI9P9C/N1EP8alezkv36gMvFzMXvm1Dx48gIODA44cOYJ27dohMzMT1atXx+bNm9GvXz8AwOXLl+Hl5YW4uDi89tprWokZYGWDiIio0lAqlcjKytJYlEplmV6bmZkJALC1tQUAJCQkoLCwEAEBAeptGjRoAFdXV8TFxWk1biYbREREYpNpZ4mMjISVlZXGEhkZ+dLDq1QqTJgwAf7+/mjUqBEAICkpCcbGxrC2ttbY1tHREUlJSVo46f/hbBQiIiKRaWs2Snh4OMLCwjTaFArFS18XEhKCCxcu4OjRo1qJo7yYbBAREVUSCoWiTMnFs0JDQ7F7927ExsaiZs2a6nYnJycUFBQgIyNDo7qRnJwMJycnbYUMgN0oREREopNiNoogCAgNDcWOHTtw8OBBuLu7a6z39fWFkZERYmJi1G1XrlzBnTt34Ofnp43TVmNlg4iISGRS3NIrJCQEmzdvxs8//wwLCwv1OAwrKyuYmprCysoKI0aMQFhYGGxtbWFpaYlx48bBz89PqzNRACYbRERE4pMg21i1ahUAoEOHDhrt69atw9ChQwEAixYtglwuR9++faFUKhEYGIiVK1dqPRbeZ4OISAK8z4buqIj7bPydnKuV/dR3rKaV/VQ0VjaIiIhEpu/PRmGyQUREJLLyDu6sajgbhYiIiETFZEMHbd28Cd3e6ISWzXwwZGB/nD93TuqQ9Bqvh+7gtZDWqV+/x9LhgYjdvErdlpOZjn1fR2HNhIFY+f5b2DIrBNdO/SFhlLpJSzcQrbSYbOiYvXt+wxdRkRgzNgRbt+2Ap2cDfDBmBNLS0qQOTS/xeugOXgtpJd+8ggtHfoV9Tc17Nfy+5nNkJN3Fm+NnYcic1fDw9ceeVfOQcvuaRJHqKD3PNphs6JiNG9ahT78BCOrdFx5162LGzNkwMTHBzp9+lDo0vcTroTt4LaRTkJ+HfV8tQKfgCVCYWWisS7r2Fxp37gWnOg1g5eCMVj0HQ1HNDCm3r0oULekiJhs6pLCgAJf+uojX/Nqo2+RyOV57rQ3OnT0jYWT6iddDd/BaSOvwd8vh1rgVXBs2L7bOqa43rp44gvzsLAgqFf6OP4zHhQWo6dlYgkh1l0xL/1VWks9GuXTpEo4fPw4/Pz80aNAAly9fxpIlS6BUKvHOO++gU6dOUodYYR5mPERRURHs7Ow02u3s7HDz5g2JotJfvB66g9dCOn/HH8aD29fw9ifLSlzf/YOPsWfVPHw1vj/kBgYwNFagR+hMWDvWqOBIdZu+z0aRNNnYu3cvevXqBXNzc+Tm5mLHjh1477330KRJE6hUKnTp0gW///77CxMOpVIJpVKp0SYYlP9BNUREpOlRegqObFmF3pMiYWhkXOI2cTs2QJmbjd6T58PE3BI3zsRhz6rP0C/8y2LjO0h/SdqNMmfOHEyZMgVpaWlYt24dBg8ejFGjRmH//v2IiYnBlClTMH/+/BfuIzIyElZWVhrL5wsiK+gMtMvG2gYGBgbFBrylpaXB3t5eoqj0F6+H7uC1kEbKrWvIy8rAltkhWDayG5aN7IZ/r5xDYszPWDayGzJS7uFczC4EDA9DLe9mqO7qgda93oGjWz2cO7hL6vB1ip6PD5U22bh48aL6/uwDBgzAo0eP0K9fP/X6IUOG4NxLpraFh4cjMzNTY5kyNVzMsEVjZGwML++GiD8ep25TqVSIj49D4ybNJIxMP/F66A5eC2nU8mqKIXNWY/CsVerFwa0+PF/rhMGzVuFxwZOqskym+atEJjeAoKpyT8L4b/Q825B8zIbs/zuy5HI5TExMYGVlpV5nYWGBzMzMF75eoSjeZVKZn43ybvAwREyfioYNG6GRT2N8t3ED8vLyENS7j9Sh6SVeD93Ba1HxjE2rwa6mm0abkcIEpmYWsKvphqLHj2Hl4IKD3y5B2wGjnnSjnD6GO3+dxlsfzpEmaB1VmQd3aoOkyYabmxuuXr0KDw8PAEBcXBxcXV3V6+/cuQNnZ2epwpNE127d8TA9HSuXL0Vq6gN4NvDCytVrYMdSsSR4PXQHr4XuMTA0RK+Jc/Hn9rX4ZelMFObnwdrBBW+MmAy3xq2kDo90iKRPfY2OjkatWrXQo0ePEtdPnz4dKSkpWLNmTbn2W5krG0SkH/jUV91REU99vZOufPlGZeBqWzknP/AR80REEmCyoTsqItm4q6Vko1YlTTZ4Uy8iIiISleQDRImIiKo63tSLiIiIRKbf2Qa7UYiIiEhUrGwQERGJjN0oREREJCo9zzXYjUJERETiYmWDiIhIZOxGISIiIlHx2ShEREQkLv3ONThmg4iIiMTFygYREZHI9LywwWSDiIhIbPo+QJTdKERERCQqVjaIiIhExtkoREREJC79zjXYjUJERETiYmWDiIhIZHpe2GCyQUREJDbORiEiIiISESsbREREIuNsFCIiIhIVu1GIiIiIRMRkg4iIiETFbhQiIiKR6Xs3CpMNIiIiken7AFF2oxAREZGoWNkgIiISGbtRiIiISFR6nmuwG4WIiIjExcoGERGR2PS8tMFkg4iISGScjUJEREQkIlY2iIiIRMbZKERERCQqPc812I1CREQkOpmWllewYsUKuLm5wcTEBK1bt8aJEyf+06m8CiYbREREVdT333+PsLAwzJw5E6dPn0aTJk0QGBiIlJSUCo2DyQYREZHIZFr6r7wWLlyIUaNGYdiwYfD29kZ0dDSqVauGb775RoSzLB2TDSIiIpHJZNpZyqOgoAAJCQkICAhQt8nlcgQEBCAuLk7LZ/hiHCBKRERUSSiVSiiVSo02hUIBhUJRbNvU1FQUFRXB0dFRo93R0RGXL18WNc7nVclkw6QKnJVSqURkZCTCw8NL/BBRxeG10B1V6VqE+LtJHcJ/UpWuRUXQ1u+lWXMjMXv2bI22mTNnYtasWdo5gEhkgiAIUgdBxWVlZcHKygqZmZmwtLSUOhy9xmuhO3gtdAevhTTKU9koKChAtWrVsH37dgQFBanbg4ODkZGRgZ9//lnscNU4ZoOIiKiSUCgUsLS01FhKqywZGxvD19cXMTEx6jaVSoWYmBj4+flVVMgAqmg3ChEREQFhYWEIDg5GixYt0KpVKyxevBg5OTkYNmxYhcbBZIOIiKiKevvtt/HgwQN88sknSEpKQtOmTbF3795ig0bFxmRDRykUCsycOZMDr3QAr4Xu4LXQHbwWlUdoaChCQ0MljYEDRImIiEhUHCBKREREomKyQURERKJiskFERESiYrJBREREomKyoYNWrFgBNzc3mJiYoHXr1jhx4oTUIeml2NhY9OzZEy4uLpDJZNi5c6fUIemtyMhItGzZEhYWFnBwcEBQUBCuXLkidVh6adWqVWjcuLH6hlJ+fn7Ys2eP1GGRjmOyoWO+//57hIWFYebMmTh9+jSaNGmCwMBApKSkSB2a3snJyUGTJk2wYsUKqUPRe0eOHEFISAiOHz+O/fv3o7CwEF26dEFOTo7UoemdmjVrYv78+UhISMCpU6fQqVMn9OrVCxcvXpQ6NNJhnPqqY1q3bo2WLVti+fLlAJ7cWrZWrVoYN24cpk2bJnF0+ksmk2HHjh0azxcg6Tx48AAODg44cuQI2rVrJ3U4es/W1haff/45RowYIXUopKNY2dAhBQUFSEhIQEBAgLpNLpcjICAAcXFxEkZGpFsyMzMBPPklR9IpKirC1q1bkZOTU+HP2qDKhXcQ1SGpqakoKioqdhtZR0dHXL58WaKoiHSLSqXChAkT4O/vj0aNGkkdjl46f/48/Pz8kJ+fD3Nzc+zYsQPe3t5Sh0U6jMkGEVUqISEhuHDhAo4ePSp1KHrL09MTiYmJyMzMxPbt2xEcHIwjR44w4aBSMdnQIfb29jAwMEBycrJGe3JyMpycnCSKikh3hIaGYvfu3YiNjUXNmjWlDkdvGRsbo27dugAAX19fnDx5EkuWLMHq1asljox0Fcds6BBjY2P4+voiJiZG3aZSqRATE8P+UNJrgiAgNDQUO3bswMGDB+Hu7i51SPQMlUoFpVIpdRikw1jZ0DFhYWEIDg5GixYt0KpVKyxevBg5OTkYNmyY1KHpnezsbFy7dk399c2bN5GYmAhbW1u4urpKGJn+CQkJwebNm/Hzzz/DwsICSUlJAAArKyuYmppKHJ1+CQ8PR7du3eDq6opHjx5h8+bNOHz4MPbt2yd1aKTDOPVVBy1fvhyff/45kpKS0LRpUyxduhStW7eWOiy9c/jwYXTs2LFYe3BwMNavX1/xAekxmUxWYvu6deswdOjQig1Gz40YMQIxMTG4f/8+rKys0LhxY0ydOhVvvPGG1KGRDmOyQURERKLimA0iIiISFZMNIiIiEhWTDSIiIhIVkw0iIiISFZMNIiIiEhWTDSIiIhIVkw0iIiISFZMNoipo6NChCAoKUn/doUMHTJgwocLjOHz4MGQyGTIyMir82ESkO5hsEFWgoUOHQiaTQSaTqR9mNWfOHDx+/FjU4/7000/49NNPy7QtEwQi0jY+G4WognXt2hXr1q2DUqnEb7/9hpCQEBgZGSE8PFxju4KCAhgbG2vlmLa2tlrZDxHRq2Blg6iCKRQKODk5oXbt2vjggw8QEBCAXbt2qbs+PvvsM7i4uMDT0xMAcPfuXQwYMADW1tawtbVFr169cOvWLfX+ioqKEBYWBmtra9jZ2eGjjz7C808heL4bRalUYurUqahVqxYUCgXq1q2LtWvX4tatW+rnwdjY2EAmk6mfPaJSqRAZGQl3d3eYmpqiSZMm2L59u8ZxfvvtN9SvXx+mpqbo2LGjRpxEpL+YbBBJzNTUFAUFBQCAmJgYXLlyBfv378fu3btRWFiIwMBAWFhY4I8//sCff/4Jc3NzdO3aVf2aL7/8EuvXr8c333yDo0ePIj09HTt27HjhMd977z1s2bIFS5cuxaVLl7B69WqYm5ujVq1a+PHHHwEAV65cwf3797FkyRIAQGRkJL799ltER0fj4sWLmDhxIt555x0cOXIEwJOkqE+fPujZsycSExMxcuRITJs2Tay3jYgqE4GIKkxwcLDQq1cvQRAEQaVSCfv37xcUCoUwefJkITg4WHB0dBSUSqV6+40bNwqenp6CSqVStymVSsHU1FTYt2+fIAiC4OzsLERFRanXFxYWCjVr1lQfRxAEoX379sKHH34oCIIgXLlyRQAg7N+/v8QYDx06JAAQHj58qG7Lz88XqlWrJhw7dkxj2xEjRgiDBg0SBEEQwsPDBW9vb431U6dOLbYvItI/HLNBVMF2794Nc3NzFBYWQqVSYfDgwZg1axZCQkLg4+OjMU7j7NmzuHbtGiwsLDT2kZ+fj+vXryMzMxP3799H69at1esMDQ3RokWLYl0pTyUmJsLAwADt27cvc8zXrl1Dbm5usceIFxQUoFmzZgCAS5cuacQBAH5+fmU+BhFVXUw2iCpYx44dsWrVKhgbG8PFxQWGhv/7NjQzM9PYNjs7G76+vti0aVOx/VSvXv2Vjm9qalru12RnZwMAfv31V9SoUUNjnUKheKU4iEh/MNkgqmBmZmaoW7dumbZt3rw5vv/+ezg4OMDS0rLEbZydnREfH4927doBAB4/foyEhAQ0b968xO19fHygUqlw5MgRBAQEFFv/tLJSVFSkbvP29oZCocCdO3dKrYh4eXlh165dGm3Hjx9/+UkSUZXHAaJEOmzIkCGwt7dHr1698Mcff+DmzZs4fPgwxo8fj3/++QcA8OGHH2L+/PnYuXMnLl++jLFjx77wHhlubm4IDg7G8OHDsXPnTvU+f/jhBwBA7dq1IZPJsHv3bjx48ADZ2dmwsLDA5MmTMXHiRGzYsAHXr1/H6dOnsWzZMmzYsAEA8P777+Pq1auYMmUKrly5gs2bN2P9+vViv0VEVAkw2SDSYdWqVUNsbCxcXV3Rp08feHl5YcSIEcjPz1dXOiZNmoR3330XwcHB8PPzg4WFBXr37v3C/a5atQr9+vXD2LFj0aBBA4waNQo5OTkAgBo1amD27NmYNm0aHB0dERoaCgD49NNPERERgcjISHh5eaFr16749ddf4e7uDgBwdXXFjz/+iJ07d6JJkyaIjo7GvHnzRHx3iKiykAmljSIjIiIi0gJWNoiIiEhUTDaIiIhIVEw2iIiISFRMNoiIiEhUTDaIiIhIVEw2iIiISFRMNoiIiEhUTDaIiIhIVEw2iIiISFRMNoiIiEhUTDaIiIhIVEw2iIiISFT/B8FsJEpCmoF+AAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "from sklearn.metrics import confusion_matrix\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "cm = confusion_matrix(y_test, log_reg.predict(X_test))\n",
        "\n",
        "sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')\n",
        "plt.xlabel(\"Predicted\")\n",
        "plt.ylabel(\"Actual\")\n",
        "plt.title(\"Confusion Matrix - Logistic Regression\")\n",
        "\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 222,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "id": "vMiE74MVOu5E",
        "outputId": "a0bf4222-cdd3-46b1-d40b-498feedbd929"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 0 Axes>"
            ]
          },
          "metadata": {}
        }
      ],
      "source": [
        "plt.savefig(\"confusion_matrix.png\", bbox_inches=\"tight\")\n",
        "plt.savefig(\"model_accuracy.png\", bbox_inches=\"tight\")"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Model Persistence**\n",
        "\n",
        "---\n",
        "\n"
      ],
      "metadata": {
        "id": "2QzG2L92R9_i"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import joblib\n",
        "\n",
        "#saving trained model\n",
        "\n",
        "joblib.dump(log_reg, \"logreg_model.pkl\")\n",
        "print(\"Model saved as logreg_model.pkl\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OwtDhx13R9lA",
        "outputId": "9e5ea0f2-8a1f-4ea9-8af1-2a0103117ac6"
      },
      "execution_count": 223,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Model saved as logreg_model.pkl\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "base",
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
      "version": "3.13.5"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
