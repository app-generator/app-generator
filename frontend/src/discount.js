import React, { useEffect, useState } from 'react';
import ProductCard from './components/Product/ProductCard';
import CardPopup from './components/Product/CardPopup';
import axios from 'axios';

const baseURL = window.location.origin;
const isAuthenticated = document
  .getElementById('app')
  .getAttribute('data-is-authenticated') === "True";


const Discount = () => {
    const [products, setProducts] = useState([]);
    const [searchQuery, setSearchQuery] = useState("");
    const [productId, setProductId] = useState("");

    const getProducts = async () => {
        try {
            const response = await axios.get(`${baseURL}/api/get-products/`);
            setProducts(response.data.products);
        } catch (error) {
            console.error("Failed to fetch products", error);
        }
    };

    const handleProductClick = (id) => {
        if (productId === id) {
            setProductId("");
        } else {
            setProductId(id);
        }
    };

    useEffect(() => {
        getProducts();
    }, []);

    const filteredProducts = products.filter(product =>
        product.name.toLowerCase().includes(searchQuery.toLowerCase())
    );

    const rows = [];
    for (let i = 0; i < filteredProducts.length; i += 3) {
    rows.push(filteredProducts.slice(i, i + 3));
    }

    return (
        <div className='mb-10 grid grid-cols-8 gap-5 items-start'>
            {/* <div className="col-span-2 p-5 bg-gray-100 rounded-2xl shadow-md">
                <h2 className="text-2xl font-semibold mb-2">Checkout</h2>
                <hr className="border-gray-300 mb-4" />

                <div className="flex items-center justify-between mb-5">
                    <p className="text-lg font-medium">Total: ${totalPriceWithHosting}</p>
                    <button
                        onClick={handlePurchase}
                        className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition"
                        disabled={loading || totalPriceWithHosting === 0}
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

                <div className="flex items-center mb-6">
                    <input onChange={handleHosting} checked={hostingChecked} id="hosting" type="checkbox" className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />
                    <label htmlFor="hosting" className="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Purchase 1year hosting</label>
                </div>

                {basket.length > 0 ? <>
                    <div className="space-y-4">
                        {basket.map((product, index) => (
                            <ProductCard product={product} key={index} callBackFunc={removeFromBasket} isBasket={true} />
                        ))}
                    </div>
                </>
                    :
                    <div className='mt-10 mb-8'>
                        <span className="block text-gray-600 text-center">Your basket is empty</span>
                        <span className="block text-gray-600 text-center">(select at least one product)</span>
                    </div>
                }
            </div> */}
            <div className="col-span-8">
                <div className="mb-5 relative flex items-center rounded-2xl p-1.5 md:p-0 overflow-hidden bg-gray-50 border border-gray-300 text-gray-900 md:col-span-1 col-span-2 dark:bg-gray-700 dark:border-gray-600">
                    <svg className="w-6 h-6 text-gray-800 dark:text-gray-400 absolute left-0 top-2/4 -translate-y-2/4 ml-1 md:ml-4 pointer-events-none"
                        aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24">
                        <path stroke="currentColor" strokeLinecap="round" strokeWidth="2" d="m21 21-3.5-3.5M17 10a7 7 0 1 1-14 0 7 7 0 0 1 14 0Z" />
                    </svg>
                    <div id="search-form" className="w-full">
                        <input type="text"
                            name="search"
                            value={searchQuery}
                            onChange={(e) => setSearchQuery(e.target.value)}
                            className="appearance-none bg-inherit !border-0 !outline-none !ring-0 h-full p-0 py-3 pl-8 md:pl-12 w-full dark:placeholder-gray-400"
                            placeholder='Search products' />
                    </div>
                    {searchQuery &&
                        <button onClick={() => setSearchQuery("")} id="clear-search" className="mr-2">
                            <svg className="w-6 h-6 text-gray-800"
                                aria-hidden="true"
                                xmlns="http://www.w3.org/2000/svg"
                                width="24"
                                height="24"
                                fill="none"
                                viewBox="0 0 24 24">
                                <path stroke="currentColor" strokeLinecap="round" stroke-linejoin="round" strokeWidth="2" d="M6 18 17.94 6M18 18 6.06 6" />
                            </svg>
                        </button>}
                </div>

                {filteredProducts.length > 0 ? (
                      <div className="space-y-5">
                        {rows.map((row, rowIndex) => (
                            <React.Fragment key={rowIndex}>
                                <div className="grid grid-cols-3 gap-5">
                                    {row.map((product) => (
                                        <ProductCard
                                            key={product.id}
                                            product={product}
                                            productId={productId}
                                            onClickFunc={handleProductClick}
                                        />
                                    ))}
                                </div>

                                {row.some((p) => p.id === productId) && (
                                    <div className="mt-5">
                                        <CardPopup 
                                            productId={productId} 
                                            baseURL={baseURL} 
                                            isAuthenticated={isAuthenticated}
                                        />
                                    </div>
                                )}
                            </React.Fragment>
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