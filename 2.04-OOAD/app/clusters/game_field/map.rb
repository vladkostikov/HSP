require_relative "cell"
require_relative "../factory/element_factory"

class Map
  WIDTH = 8
  HEIGHT = 8

  attr_reader :width, :height

  def initialize(grid = nil)
    @grid = grid || Array.new(HEIGHT) do |y|
      Array.new(WIDTH) do |x|
        Cell.new(x, y)
      end
    end
    @height = @grid.size
    @width = @grid[0].size
  end

  def cell_at(x, y)
    return nil if x.negative? || x >= WIDTH || y.negative? || y >= HEIGHT

    @grid[y][x]
  end

  def swap(cell1, cell2)
    # Проверяем, что обе клетки существуют и соседние
    return false unless cell1 && cell2
    return false unless adjacent?(cell1, cell2)

    # Меняем элементы
    e1 = cell1.element
    e2 = cell2.element

    cell1.insert_element(e2, force: true)
    cell2.insert_element(e1, force: true)
    true
  end

  def each_cell(&)
    @grid.flatten.each(&)
  end

  def adjacent?(cell1, cell2)
    (cell1.x - cell2.x).abs + (cell1.y - cell2.y).abs == 1
  end

  def fill_top_row_empty_cells(factory)
    top_row = @grid[0]

    top_row.each do |cell|
      cell.insert_element(factory.create_random, force: true) if cell.empty?
    end
  end

  def all_matches
    raw_matches = horizontal_matches + vertical_matches
    merged_matches = []

    raw_matches.each do |match|
      overlapping = merged_matches.select do |group|
        group.intersect?(match)
      end

      if overlapping.empty?
        merged_matches << match
      else
        combined = overlapping.flatten.uniq + match
        combined.uniq!

        merged_matches.reject! { |group| overlapping.include?(group) }

        merged_matches << combined
      end
    end

    merged_matches
  end

  def has_matches?
    horizontal_matches.any? || vertical_matches.any?
  end

  def remove_matches!
    matches = horizontal_matches + vertical_matches

    matches.each do |match|
      match.each(&:clear)
    end
  end

  def has_empty_cells?
    each_cell do |cell|
      return true if cell.empty?
    end
    false
  end

  def has_possible_moves?
    (0...width).each do |x|
      (0...height).each do |y|
        current_cell = cell_at(x, y)
        neighbors = adjacent_cells(x, y)

        neighbors.each do |neighbor|
          swap(current_cell, neighbor)
          if has_matches?
            swap(current_cell, neighbor)
            return true
          end
          swap(current_cell, neighbor)
        end
      end
    end
    false
  end

  def adjacent_cells(x, y)
    neighbors = []
    neighbors << cell_at(x + 1, y) if x + 1 < width
    neighbors << cell_at(x - 1, y) if x - 1 >= 0
    neighbors << cell_at(x, y + 1) if y + 1 < height
    neighbors << cell_at(x, y - 1) if y - 1 >= 0
    neighbors.compact
  end

  private

  def horizontal_matches
    matches = []

    @height.times do |y|
      match = [@grid[y][0]]

      (1...@width).each do |x|
        current = @grid[y][x]
        previous = @grid[y][x - 1]

        if current.match?(previous)
          match << current
        else
          matches << match if match.size >= 3
          match = [current]
        end
      end

      matches << match if match.size >= 3
    end

    matches
  end

  def vertical_matches
    matches = []

    @width.times do |x|
      match = [@grid[0][x]]

      (1...@height).each do |y|
        current = @grid[y][x]
        previous = @grid[y - 1][x]

        if current.match?(previous)
          match << current
        else
          matches << match if match.size >= 3
          match = [current]
        end
      end

      matches << match if match.size >= 3
    end

    matches
  end
end
