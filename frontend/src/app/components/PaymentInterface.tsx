"use client"
import { useState } from 'react';

interface Friend {
  id: number;
  name: string;
}

export default function PaymentInterface() {
  const [friends, setFriends] = useState<Friend[]>([
    { id: 1, name: 'Maria' },
    { id: 2, name: 'Carlos' },
    { id: 3, name: 'Luis' },
  ]);

  const [selectedFriend, setSelectedFriend] = useState<string>('');
  const [amount, setAmount] = useState<string>('');

  const handlePay = () => {
    if (!selectedFriend || !amount) {
      alert('Por favor, selecciona un amigo e introduce un monto válido.');
      return;
    }

    alert(`Pago registrado:\nAmigo: ${selectedFriend}\nMonto: $${amount}`);
  };

  return (
    <div className="max-w-lg mx-auto my-10 p-6 shadow-md rounded-lg border border-gray-200 bg-white">
      <h2 className="text-2xl font-bold mb-4 text-gray-800">Pago</h2>

      <div className="mb-4">
        <label htmlFor="friends" className="block text-sm font-medium text-gray-700 mb-2">
          Selecciona un amigo:
        </label>
        <select
          id="friends"
          value={selectedFriend}
          onChange={(e) => setSelectedFriend(e.target.value)}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
        >
          <option value="">-- Selecciona un amigo --</option>
          {friends.map((friend) => (
            <option key={friend.id} value={friend.name}>
              {friend.name}
            </option>
          ))}
        </select>
      </div>

      <div className="mb-4">
        <label htmlFor="amount" className="block text-sm font-medium text-gray-700 mb-2">
          Monto a pagar:
        </label>
        <input
          id="amount"
          type="number"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
          placeholder="Introduce el monto"
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
        />
      </div>

      <button
        onClick={handlePay}
        className="w-full py-2 px-4 bg-blue-500 text-white text-sm font-medium rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-50"
      >
        Pagar
      </button>
    </div>
  );
}