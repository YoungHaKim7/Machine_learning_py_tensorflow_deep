import pandas as pd


def main():
    # Create a sample DataFrame
    data = {
        "Name": ["John", "Anna", "Peter", "Linda"],
        "Age": [28, 24, 35, 32],
        "Country": ["USA", "UK", "Australia", "Germany"],
    }
    df = pd.DataFrame(data)

    # Print the DataFrame
    print(df)

    # Add a new column
    df["City"] = ["New York", "London", "Sydney", "Berlin"]

    # Print the updated DataFrame
    print(df)

    # Filter rows where Age is greater than 30
    filtered_df = df[df["Age"] > 30]
    print(filtered_df)

    # Group by Country and calculate the mean Age
    grouped_df = df.groupby("Country")["Age"].mean()
    print(grouped_df)


if __name__ == "__main__":
    main()
