require_relative "../bonus"

class CrossBonus < Bonus
  def activate(game_map, cell)
    cleared_cells = []

    positions = [
      [cell.x, cell.y],
      [cell.x - 1, cell.y],
      [cell.x + 1, cell.y],
      [cell.x, cell.y - 1],
      [cell.x, cell.y + 1]
    ]

    positions.each do |x, y|
      target = game_map.cell_at(x, y)
      next if target.nil?

      target.clear
      cleared_cells << target
    end

    cleared_cells
  end
end
