from random import choice
from re import X

class RandomWalk:
  """ランダムウォークを生成するためのクラス"""
  def __init__(self,num_points=5000):
    """ランダムウォークの属性を初期化"""
    self.num_points = num_points

    # 全てのランダムウォークは(0,0)から開始
    self.x_values = [0]
    self.y_values = [0]

  def fill_walk(self):
    """ランダムウォークの全ての点を計算"""
    # ステップ数が指定した数になるまでランダムウォークを続ける
    while len(self.x_values) < self.num_points:

      # 移動する方向と距離を決定
      x_step = self.get_step()
      y_step = self.get_step()

      # どこにも移動しない場合は結果を破棄
      if x_step == 0 and y_step == 0:
        continue

      # 新しい位置を計算する
      x = self.x_values[-1] + x_step
      y = self.y_values[-1] + y_step

      self.x_values.append(x)
      self.y_values.append(y)

  def get_step(self):
    direction = choice([1,-1])
    distance = choice([0,1,2,3,4])
    step = direction * distance
    return step
