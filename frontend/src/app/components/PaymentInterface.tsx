"use client"
import {useEffect, useState} from 'react';
import {fetchAccountFriend, fetchListFriends} from "@/lib/api";

interface Friend {
    id: number;
    name: string;
}

export default function PaymentInterface() {
    const [friends, setFriends] = useState<Friend[]>([]);
    const [selectedFriend, setSelectedFriend] = useState<string>('');
    const [amount, setAmount] = useState<string>('');
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);
    const [amountLoading, setAmountLoading] = useState<boolean>(false);

    useEffect(() => {
        const loadFriends = async () => {
            try {
                const data = await fetchListFriends();
                setFriends(data);
                setLoading(false);
            } catch (err: any) {
                setError('Error al cargar la lista de amigos');
                setLoading(false);
            }
        };

        loadFriends();
    }, []);

    const handleFriendSelection = async (friendName: string) => {
        setSelectedFriend(friendName);
        setAmount('');

        if (!friendName) return;

        setAmountLoading(true);
        try {
            const {total_account} = await fetchAccountFriend(friendName);
            setAmount(total_account.toString());
        } catch (error) {
            console.error('Error al obtener la cuenta del amigo:', error);
            alert('Error al obtener el monto del amigo seleccionado. Inténtalo de nuevo.');
        } finally {
            setAmountLoading(false);
        }
    };

    const handlePay = () => {
        if (!selectedFriend || !amount) {
            alert('Por favor, selecciona un amigo e introduce un monto válido.');
            return;
        }

        alert(`Pago registrado:\nAmigo: ${selectedFriend}\nMonto: $${amount}`);
    };

    if (loading) {
        return (
            <div
                className="max-w-lg mx-auto my-10 p-6 shadow-md rounded-lg border border-gray-200 bg-white text-center">
                <p className="text-gray-600">Cargando la lista de amigos...</p>
            </div>
        );
    }

    if (error) {
        return (
            <div
                className="max-w-lg mx-auto my-10 p-6 shadow-md rounded-lg border border-gray-200 bg-white text-center">
                <p className="text-red-600">{error}</p>
            </div>
        );
    }

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
                    onChange={(e) => handleFriendSelection(e.target.value)}
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
                    placeholder={amountLoading ? 'Cargando...' : 'Introduce el monto'}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
                    disabled={amountLoading}
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