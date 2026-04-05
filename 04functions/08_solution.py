def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
        
print_kwargs(name="Vinay", score=100)
print_kwargs(name="Vinay Kumar")