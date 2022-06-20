class CreateWays < ActiveRecord::Migration[7.0]
  def change
    create_table :ways do |t|
      t.integer :steps
      t.references :stand, null: false, foreign_key: true

      t.timestamps
    end
  end
end
