# -*- coding: utf-8 -*-
"""Serial.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SZ4UtEpdPlVK4siej050WzYuQKFE27QM
"""

import pandas as pd
import time
students_file_path = "students.csv"
fees_file_path = "student_fees.csv"
def read_students_csv():
    return pd.read_csv(students_file_path)
def read_fees_csv():
    return pd.read_csv(fees_file_path)
start_time = time.time()
students_df = read_students_csv()
fees_df = read_fees_csv()
end_time = time.time()
print(f"Serial Execution Time: {end_time - start_time:.4f} seconds")