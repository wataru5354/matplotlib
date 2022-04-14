import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:
  #ランダムウォークを生成する
  rw = RandomWalk()
  rw.fill_walk()

  # ランダムウォークの点を描画する
  plt.style.use('classic')
  fig, ax = plt.subplots(figsize=(15,9))
  point_numbers = range(rw.num_points)
  ax.plot(rw.x_values,rw.y_values,linewidth=1)

  # 軸の削除
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)
  plt.show()

  keep_running = input("別のランダムウォークを生成する？(y/n): ")
  if keep_running == 'n':
    break