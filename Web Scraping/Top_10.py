from tabulate import tabulate

GM = [ [1, 'Carlsen, Magnus', 'NOR', 2859, 1990],
      [2, "Ding, Liren", 'CHN', 2811, 1992],
      [3, 'Nepomniachtchi, Ian','RUS', 	2793, 1990],
      [4, "Firouzja, Alireza", 'FRA', 2785, 2003],
      [5, "Nakamura, Hikaru", 'USA', 2768, 1987],
      [6, "Caruana, Fabiano", 'USA', 2766, 1992],
      [7, "Giri, Anish", 'NED', 2764, 1994],
      [8, "So, Wesley", 'USA', 2760, 1993],
      [9, "Anand, Viswanathan", 'IND', 2754, 1969],
      [10, "Karjakin, Sergey", 'RUS', 2747, 1990],
      ]

print(tabulate(GM, headers=['Rating','Name','Fed', 'Elo','B-Year']))
