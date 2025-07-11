require_relative "../bonus"

class RowBonus < Bonus
  def activate(game_map, cell)
    y = cell.y
    cleared_cells = []

    (0...game_map.width).each do |x|
      target = game_map.cell_at(x, y)
      next if target.nil?

      target.clear
      cleared_cells << target
    end

    cleared_cells
  end
end
