import { useEffect, useState } from 'react'
import axios from 'axios'

function App() {
  const [items, setItems] = useState([])
  const [loading, setLoading] = useState(true)
  const [newItem, setNewItem] = useState({ name: '', description: '' })

  useEffect(() => {
    fetchItems()
  }, [])

  const fetchItems = async () => {
    try {
      const response = await axios.get('/api/items')
      setItems(response.data)
    } catch (error) {
      console.error('Error fetching data:', error)
    } finally {
      setLoading(false)
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      await axios.post('/api/items', newItem)
      setNewItem({ name: '', description: '' })
      await fetchItems()
    } catch (error) {
      console.error('Error creating item:', error)
    }
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6">Items Manager</h1>
      
      <form onSubmit={handleSubmit} className="mb-8 p-4 bg-gray-50 rounded-lg">
        <div className="mb-4">
          <label className="block text-sm font-medium mb-1">Name</label>
          <input
            type="text"
            value={newItem.name}
            onChange={(e) => setNewItem({...newItem, name: e.target.value})}
            className="w-full p-2 border rounded"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium mb-1">Description</label>
          <input
            type="text"
            value={newItem.description}
            onChange={(e) => setNewItem({...newItem, description: e.target.value})}
            className="w-full p-2 border rounded"
          />
        </div>
        <button
          type="submit"
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Add Item
        </button>
      </form>

      {loading ? (
        <p className="text-gray-600">Loading items...</p>
      ) : (
        <div className="space-y-4">
          {items.map((item) => (
            <div key={item._id} className="p-4 bg-white rounded-lg shadow">
              <h3 className="text-lg font-semibold">{item.name}</h3>
              {item.description && (
                <p className="text-gray-600 mt-1">{item.description}</p>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default App