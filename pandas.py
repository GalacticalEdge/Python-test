print("This is pandas basics")

def pandas():
    import pandas as pd

dict = {"country": ["Brazil", "India", "China", "South Africa"], 
        "capital": ["Brasilia", "New Dehli", "Beijing", "Pretoria"], 
        "area": [8.516, 3.286, 9.597, 1.221], 
        "population": [200.4, 1252, 1357, 52.98] 
       }

brics = pd.DataFrame(dict)
print(brics)