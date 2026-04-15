#-----removes empty rows-----
def delete_empty(df):
    #checks and sums all the number of missing values
    missing_values = df.isnull().sum().sum()

    #deletes the missing values
    clean_data=df.dropna(subset=["PTS","Team","Player","Season"] )
    print("There is a total of ", missing_values, " missing values in this dataset")
    return clean_data

#------filters data based on users choice----
def filter_data(df):
    print("1.only players with PTS > X")
    print("2.only one team")
    print("3.only one season")
    try:
        choice = int(input("pick 1-3:"))
        
        if (choice == 1 ):
            X=int(input("state the minimum point you want: "))
            filtered_df = df[df["PTS"] > X]
            return filtered_df
                
        elif (choice == 2 ):
            team = input("enter team name:")
            filtered_df = df[df["Team"] == team]
            return filtered_df
            
        elif (choice == 3 ):
            season = input("enter the season:")
            filtered_df = df[df["Season"] == season]
            return filtered_df
    except Exception as e:
        print("Invalid input:",e)
        return df

#------Create new column based on existing ones----     
def create_column(df):
    new_column_name = input("enter a name for the new column: ")
    expression = input("enter an expression for the new column: ")
    try:
        df[new_column_name] = df.eval(expression)
        return df
    except Exception as e:
        print("creating the new column failed:",e)
    return df
