# Uncovering the Mesoscale Structure of the Credit Default Swap Market

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Research](https://img.shields.io/badge/Research-Paper-brightgreen.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

## Overview

This repository contains the Python implementation of the methodology proposed in the research paper **"Uncovering the mesoscale structure of the credit default swap market to improve portfolio risk modelling"** by Ioannis Anagnostou, Tiziano Squartini, Drona Kandhai, and Diego Garlaschelli. The paper introduces a novel approach to uncover the mesoscopic structure of the Credit Default Swap (CDS) market using Random Matrix Theory (RMT) and modular decomposition techniques. 

The key idea is to identify groups of issuers in the CDS market that exhibit strong internal correlation and mutual anti-correlation, revealing a hierarchical organization that goes beyond traditional industry/region taxonomies. This mesoscopic decomposition is then leveraged to develop an advanced portfolio risk model that outperforms traditional alternatives.

The repository provides a Python script (`implementation.py`) to reproduce the methodology and results, enabling researchers, analysts, and financial professionals to explore the hidden structure of the CDS market and improve portfolio risk modeling.

---

## How It Works

The implementation follows the steps outlined in the paper to uncover the mesoscale structure of the CDS market:

### 1. **Data Preprocessing**
   - The input data consists of time series of CDS spreads for various financial entities.
   - The correlation matrix is computed from the time series data to capture relationships between entities.

### 2. **Random Matrix Theory (RMT) Filtering**
   - RMT is applied to the correlation matrix to filter out noise and identify statistically significant correlations.
   - The eigenvalues of the correlation matrix are analyzed to separate signal from noise, based on theoretical RMT predictions.

### 3. **Hierarchical Modularity Detection**
   - A modular decomposition technique is applied to the filtered correlation matrix to detect communities of issuers.
   - These communities represent groups of entities with strong internal correlation and mutual anti-correlation, revealing the mesoscale structure of the market.

### 4. **Portfolio Risk Modeling**
   - The identified mesoscopic structure is used to develop a novel default risk model.
   - This model accounts for the hierarchical organization of the market, improving risk estimation compared to traditional factor models.

---

## Installation

To use the implementation, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/CDS-mesoscale-structure.git
   cd CDS-mesoscale-structure
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

The main implementation is contained in the `implementation.py` script. Below are the instructions for running the script:

### Input Data
- The script expects a CSV file containing time series data of CDS spreads for various financial entities.
- The file should have the following format:
  - Rows represent time points.
  - Columns represent different entities.
  - Each cell contains the CDS spread for a specific entity at a specific time.

### Running the Script
1. Execute the script with the following command:
   ```bash
   python implementation.py --input_file data/cds_data.csv --output_dir results/
   ```
   - `--input_file`: Path to the input CSV file containing CDS time series data.
   - `--output_dir`: Directory where the results will be saved.

2. The script will perform the following tasks:
   - Compute the correlation matrix from the input data.
   - Apply RMT filtering to extract the significant correlations.
   - Perform hierarchical modularity detection to uncover the mesoscopic structure.
   - Save the identified communities and their hierarchical organization to the output directory.
   - Generate visualizations of the mesoscopic structure.

### Output
- The script will produce the following outputs in the specified `output_dir`:
  - **Filtered Correlation Matrix**: A CSV file containing the RMT-filtered correlation matrix.
  - **Community Assignments**: A CSV file mapping each entity to its detected community.
  - **Hierarchical Structure Visualization**: A dendrogram or graph representation of the mesoscale structure.
  - **Portfolio Risk Metrics**: A report comparing the performance of the novel risk model with traditional models.

---

## Example

Here is an example of running the script with sample data:

```bash
python implementation.py --input_file data/sample_cds_data.csv --output_dir results/
```

After execution, check the `results/` directory for the output files and visualizations.

---

## Dependencies

The script requires the following Python libraries:
- `numpy`
- `pandas`
- `matplotlib`
- `scipy`
- `networkx`

Install all dependencies using the provided `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

## Contributing

We welcome contributions to improve this implementation! If you would like to contribute:
1. Fork this repository.
2. Create a new branch (`feature/your-feature-name`).
3. Commit your changes.
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## References

- Ioannis Anagnostou, Tiziano Squartini, Drona Kandhai, Diego Garlaschelli. *Uncovering the mesoscale structure of the credit default swap market to improve portfolio risk modelling*. [arXiv:2006.03014v2](https://arxiv.org/pdf/2006.03014v2)

---

## Contact

For questions, feedback, or collaboration opportunities, feel free to reach out:
- **Email**: your_email@example.com
- **GitHub**: [yourusername](https://github.com/yourusername)

---

## Acknowledgements

We thank the authors of the research paper for their groundbreaking work in uncovering the mesoscale structure of financial markets. Their methodology has inspired this implementation, which aims to make their findings accessible to a broader audience.