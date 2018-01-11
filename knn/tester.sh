#IRIS DATASET

# Brak normalizacji

# Metryka euklidesowa

./main.py --neighbours=1 --metrics=euclidean --dataset="datasets/iris.csv"
./main.py --neighbours=3 --metrics=euclidean --dataset="datasets/iris.csv"
./main.py --neighbours=5 --metrics=euclidean --dataset="datasets/iris.csv"
./main.py --neighbours=10 --metrics=euclidean --dataset="datasets/iris.csv"

# Metryka manhattan

./main.py --neighbours=1 --metrics=manhattan --dataset="datasets/iris.csv"
./main.py --neighbours=3 --metrics=manhattan --dataset="datasets/iris.csv"
./main.py --neighbours=5 --metrics=manhattan --dataset="datasets/iris.csv"
./main.py --neighbours=10 --metrics=manhattan --dataset="datasets/iris.csv"

# Metryka Czebyszewa

./main.py --neighbours=1 --metrics=chebyshev --dataset="datasets/iris.csv"
./main.py --neighbours=3 --metrics=chebyshev --dataset="datasets/iris.csv"
./main.py --neighbours=5 --metrics=chebyshev --dataset="datasets/iris.csv"
./main.py --neighbours=10 --metrics=chebyshev --dataset="datasets/iris.csv"

# Normalizacja

./main.py --neighbours=1 --metrics=euclidean --dataset="datasets/iris.csv" --normalize
./main.py --neighbours=3 --metrics=euclidean --dataset="datasets/iris.csv" --normalize
./main.py --neighbours=5 --metrics=euclidean --dataset="datasets/iris.csv" --normalize
./main.py --neighbours=10 --metrics=euclidean --dataset="datasets/iris.csv" --normalize

# Metryka manhattan

./main.py --neighbours=1 --metrics=manhattan --dataset="datasets/iris.csv" --normalize
./main.py --neighbours=3 --metrics=manhattan --dataset="datasets/iris.csv" --normalize
./main.py --neighbours=5 --metrics=manhattan --dataset="datasets/iris.csv" --normalize
./main.py --neighbours=10 --metrics=manhattan --dataset="datasets/iris.csv" --normalize

# Metryka Czebyszewa

./main.py --neighbours=1 --metrics=chebyshev --dataset="datasets/iris.csv" --normalize
./main.py --neighbours=3 --metrics=chebyshev --dataset="datasets/iris.csv" --normalize
./main.py --neighbours=5 --metrics=chebyshev --dataset="datasets/iris.csv" --normalize
./main.py --neighbours=10 --metrics=chebyshev --dataset="datasets/iris.csv" --normalize


# WINE DATASET

# Brak normalizacji

# Metryka euklidesowa

./main.py --neighbours=1 --metrics=euclidean --dataset="datasets/wine.csv"
./main.py --neighbours=3 --metrics=euclidean --dataset="datasets/wine.csv"
./main.py --neighbours=5 --metrics=euclidean --dataset="datasets/wine.csv"
./main.py --neighbours=10 --metrics=euclidean --dataset="datasets/wine.csv"

# Metryka manhattan

./main.py --neighbours=1 --metrics=manhattan --dataset="datasets/wine.csv"
./main.py --neighbours=3 --metrics=manhattan --dataset="datasets/wine.csv"
./main.py --neighbours=5 --metrics=manhattan --dataset="datasets/wine.csv"
./main.py --neighbours=10 --metrics=manhattan --dataset="datasets/wine.csv"

# Metryka Czebyszewa

./main.py --neighbours=1 --metrics=chebyshev --dataset="datasets/wine.csv"
./main.py --neighbours=3 --metrics=chebyshev --dataset="datasets/wine.csv"
./main.py --neighbours=5 --metrics=chebyshev --dataset="datasets/wine.csv"
./main.py --neighbours=10 --metrics=chebyshev --dataset="datasets/wine.csv"

# Normalizacja

./main.py --neighbours=1 --metrics=euclidean --dataset="datasets/wine.csv" --normalize
./main.py --neighbours=3 --metrics=euclidean --dataset="datasets/wine.csv" --normalize
./main.py --neighbours=5 --metrics=euclidean --dataset="datasets/wine.csv" --normalize
./main.py --neighbours=10 --metrics=euclidean --dataset="datasets/wine.csv" --normalize

# Metryka manhattan

./main.py --neighbours=1 --metrics=manhattan --dataset="datasets/wine.csv" --normalize
./main.py --neighbours=3 --metrics=manhattan --dataset="datasets/wine.csv" --normalize
./main.py --neighbours=5 --metrics=manhattan --dataset="datasets/wine.csv" --normalize
./main.py --neighbours=10 --metrics=manhattan --dataset="datasets/wine.csv" --normalize

# Metryka Czebyszewa

./main.py --neighbours=1 --metrics=chebyshev --dataset="datasets/wine.csv" --normalize
./main.py --neighbours=3 --metrics=chebyshev --dataset="datasets/wine.csv" --normalize
./main.py --neighbours=5 --metrics=chebyshev --dataset="datasets/wine.csv" --normalize
./main.py --neighbours=10 --metrics=chebyshev --dataset="datasets/wine.csv" --normalize
