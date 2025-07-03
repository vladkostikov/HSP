require_relative 'cell'
require_relative '../factory/element_factory'

class Map
  WIDTH = 8
  HEIGHT = 8

  def initialize(factory = ElementFactory.new)
    @factory = factory
    @grid = Array.new(HEIGHT) do |y|
      Array.new(WIDTH) do |x|
        Cell.new(x, y, @factory.create_random_element)
      end
    end
  end

  def cell_at(x, y)
    return nil if x < 0 || x >= WIDTH || y < 0 || y >= HEIGHT
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

  def each_cell(&block)
    @grid.flatten.each(&block)
  end

  private

  def adjacent?(cell1, cell2)
    (cell1.x - cell2.x).abs + (cell1.y - cell2.y).abs == 1
  end
end
