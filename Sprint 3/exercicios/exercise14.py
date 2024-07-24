def variable(*args, **kwargs):	
    for item in args:
        print(item)
    for item, dado in kwargs.items():
        print(dado)
        
variable(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
