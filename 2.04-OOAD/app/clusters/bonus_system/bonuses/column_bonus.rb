require_relative "../bonus"

class ColumnBonus < Bonus
  def activate(game_map, cell)
    x = cell.x
    cleared_cells = []

    (0...game_map.height).each do |y|
      c = game_map.cell_at(x, y)
      cleared_cells << c unless c.nil?
      c&.clear
    end

    cleared_cells
  end
end
