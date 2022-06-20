class CreateStands < ActiveRecord::Migration[7.0]
  def change
    create_table :stands do |t|
      t.integer :area
      t.string :brand

      t.timestamps
    end
  end
end
