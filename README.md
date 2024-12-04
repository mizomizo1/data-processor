# README

## DataProcessor Class

This repository contains a Python script implementing a `DataProcessor` class for data preprocessing and manipulation. It is designed to handle and preprocess student data for tasks such as updating survey submissions with the latest information from a primary dataset.

## Features

1. **Data Preprocessing**:
   - Identifies unique rows based on an `id` column.
   - Handles duplicate `id` entries by keeping only the latest record based on a `time` column.
   - Combines unique and latest records into a clean dataset.

2. **Submission Data Update**:
   - Matches `id` values from a submission dataset to the cleaned data.
   - Updates `NG_1` and `NG_2` fields in the submission dataset based on the latest data.

3. **Easy Integration**:
   - Processes data from two CSV files and returns cleaned and updated DataFrames for further use.


## File Descriptions

- **`data/`**: Directory to store the input datasets.
  - `臨床実習アンケート.csv`: Main dataset with student information and timestamps.
  - `NG調査報告_95期.csv`: Submission dataset to be updated.
  
- **`data_processor.py`**: Script containing the `DataProcessor` class.


## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/data-processor.git
   cd data-processor
   ```

2. **Install dependencies**:
   This script uses the following Python libraries:
   - `pandas`
   - `numpy`
   - `warnings`

   Install them using pip if not already installed:
   ```bash
   pip install pandas numpy
   ```

3. **Setup Google Drive (Optional)**:
   If running in Google Colab, ensure you have access to your Google Drive and replace file paths accordingly.


## Usage

1. **Prepare Your Data**:
   Ensure the `data_path` and `submit_path` point to valid CSV files in your environment.

2. **Run the Script**:
   ```python
   from data_processor import DataProcessor
   
   data_path = 'path/to/臨床実習アンケート.csv'
   submit_path = 'path/to/NG調査報告_95期.csv'

   processor = DataProcessor(data_path, submit_path)
   df, df_submit = processor.get_processed_data()
   ```

3. **Access Processed Data**:
   - `df`: Cleaned primary dataset.
   - `df_submit`: Updated submission dataset.

4. **Inspect Data**:
   ```python
   df.info()
   df_submit.info()
   ```
   
## Customization

- **Change File Paths**:
   Modify `data_path` and `submit_path` in the script to match your dataset locations.
   
- **Add New Columns**:
   Extend the `update_submit_data` method to include other columns if necessary.


## Example

```python
data_path = '/path/to/臨床実習アンケート.csv'
submit_path = '/path/to/NG調査報告_95期.csv'

processor = DataProcessor(data_path, submit_path)
df, df_submit = processor.get_processed_data()

# Save the updated datasets
df.to_csv('cleaned_data.csv', index=False)
df_submit.to_csv('updated_submission.csv', index=False)
```


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any issues or inquiries, feel free to create an issue in this repository.
