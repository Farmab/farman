import pandas as pd
import streamlit as st
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt

# Load the dataset
data_file = "iphone.csv"
try:
    data = pd.read_csv(data_file)
except FileNotFoundError:
    st.error("The file 'iphone.csv' was not found. Please ensure it exists in the same directory.")

# Streamlit app
def main():
    st.title("iPhone Inventory Visualization")

    if 'data' in globals():
        # Display dataset
        st.subheader("Dataset")
        st.dataframe(data)

        # Visualizations
        st.subheader("Visualizations")

        # Total Quantity by Model
        st.write("### Total Quantity by Model")
        try:
            total_by_model = data.groupby('Model')['Total Quantity'].sum()
            fig1, ax1 = plt.subplots()
            total_by_model.plot(kind='bar', color='skyblue', ax=ax1)
            ax1.set_title('Total Quantity by Model')
            ax1.set_xlabel('Model')
            ax1.set_ylabel('Total Quantity')
            st.pyplot(fig1)
        except Exception as e:
            st.error(f"Error plotting Total Quantity by Model: {e}")

        # Sold vs Remaining by Model
        st.write("### Sold vs Remaining by Model")
        try:
            sold_vs_remaining = data.groupby('Model')[['Sold', 'Remaining']].sum()
            fig2, ax2 = plt.subplots()
            sold_vs_remaining.plot(kind='bar', stacked=True, ax=ax2, color=['orange', 'green'])
            ax2.set_title('Sold vs Remaining by Model')
            ax2.set_xlabel('Model')
            ax2.set_ylabel('Quantity')
            st.pyplot(fig2)
        except Exception as e:
            st.error(f"Error plotting Sold vs Remaining by Model: {e}")

        # Quantity by Color
        st.write("### Total Quantity by Color")
        try:
            total_by_color = data.groupby('Color')['Total Quantity'].sum()
            fig3, ax3 = plt.subplots()
            total_by_color.plot(kind='bar', color='purple', ax=ax3)
            ax3.set_title('Total Quantity by Color')
            ax3.set_xlabel('Color')
            ax3.set_ylabel('Total Quantity')
            st.pyplot(fig3)
        except Exception as e:
            st.error(f"Error plotting Total Quantity by Color: {e}")
    else:
        st.error("Data could not be loaded. Please check the CSV file.")

if __name__ == "__main__":
    main()
