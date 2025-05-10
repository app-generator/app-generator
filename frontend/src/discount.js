import React, { useEffect, useState } from 'react';
import ProductCard from './components/Product/ProductCard';
import { MultiSelect } from "react-multi-select-component";
import axios from 'axios';

const baseURL = window.location.origin;

const Discount = () => {
    const [products, setProducts] = useState([]);
    const [selectedProducts, setSelectedProducts] = useState([]);
    const [filteredProducts, setFilteredProducts] = useState([]);
    const [basket, setBasket] = useState([]);
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState("");

    const getProducts = async () => {
        try {
            const response = await axios.get(`${baseURL}/api/get-products/`);
            setProducts(response.data.products);
            setFilteredProducts(response.data.products);
        } catch (error) {
            console.error("Failed to fetch products", error);
        }
    };


    const options = products.map((product) => ({
        label: product.name,
        value: product.id,
    }));


    useEffect(() => {
        if (selectedProducts.length === 0) {
            setFilteredProducts(products);
        } else {
            const selectedIds = selectedProducts.map((item) => item.value);
            const filtered = products.filter((product) =>
                selectedIds.includes(product.id)
            );
            setFilteredProducts(filtered);
        }
    }, [selectedProducts, products]);

    const totalPrice = basket.reduce((sum, product) => sum + product.price, 0);

    const addToBasket = (product) => {
        setBasket([...basket, product]);
    };

    const removeFromBasket = (productId) => {
        setBasket(basket.filter(item => item.id !== productId));
    };

    const handlePurchase = async () => {
        if (basket.length === 0) {
            setMessage("Your basket is empty (select at least one product)");
            setTimeout(() => setMessage(""), 3000);
            return;
        }

        setLoading(true)
        try {
            const response = await axios.post(`${baseURL}/api/create-checkout-session/`, {
                basket: basket,
            });

            const sessionUrl = response.data.url;
            window.location.href = sessionUrl;
        } catch (error) {
            console.error("Failed to initiate checkout", error);
        } finally {
            setLoading(false)
        }
    };


    useEffect(() => {
        getProducts();
    }, []);


    return (
        <div className='mb-10 grid grid-cols-7 gap-5'>
            <div className="col-span-2 p-5 bg-white rounded-2xl shadow-md">
                <h2 className="text-2xl font-semibold mb-2">Checkout</h2>
                <hr className="border-gray-300 mb-4" />

                <div className="flex items-center justify-between mb-6">
                    <p className="text-lg font-medium">Total: ${totalPrice}</p>
                    <button
                        onClick={handlePurchase}
                        className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition"
                        disabled={loading}
                    >
                        {!loading ? 'Purchase' : <>
                            <div role="status">
                                <svg aria-hidden="true" className="w-4 h-4 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor" />
                                    <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill" />
                                </svg>
                                <span className="sr-only">Loading...</span>
                            </div>
                        </>}
                    </button>
                </div>

                <div className="space-y-4">
                    {basket.map((product, index) => (
                        <ProductCard product={product} key={index} callBackFunc={removeFromBasket} basket={true} />
                    ))}

                    {message && (
                        <p className="text-red-600 text-center mt-10">{message}</p>
                    )}
                </div>
            </div>
            <div className="col-span-5">
                <form className=" mb-10" method="get">
                    <MultiSelect
                        options={options}
                        value={selectedProducts}
                        onChange={setSelectedProducts}
                        labelledBy="Select products"
                        className='w-full'
                    />
                </form>

                {filteredProducts.length > 0 ? (
                    <div className="grid grid-cols-3 gap-5">
                        {filteredProducts.map((product, index) => (
                            <ProductCard product={product} key={index} callBackFunc={addToBasket} />
                        ))}
                    </div>
                ) : (
                    <div className="flex items-center justify-center w-full h-64 my-8">
                        <p className="text-gray-600 dark:text-white">No products found</p>
                    </div>
                )}
            </div>
        </div>
    )
}

export default Discount