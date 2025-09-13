import React, { useEffect, useState } from 'react';
import axios from 'axios';

const CardPopup = ({ productId, baseURL }) => {
    const [product, setProduct] = useState({});

    useEffect(() => {
        if (productId) {
                const productDetails = async () => {
                    try {
                        const response = await axios.get(`${baseURL}/api/product/${productId}`);
                        setProduct(response?.data?.product);
                    } catch (error) {
                        console.error("Failed to fetch products", error);
                    }
                };

                productDetails();
        }
    }, [productId])

    return (
        <section className="max-w-screen-xl mx-3 md:mx-auto border border-gray-200 dark:border-gray-700 rounded-lg p-3 md:p-8 flex justify-between gap-10 shadow-md flex-col md:flex-row">
            <div className="basis-1/2 flex items-start justify-center flex-col">
                <h5 className="text-gray-900 dark:text-white font-bold text-xl md:text-2xl mb-3">
                    <a 
                        href={
                            product.tech2 && product.tech2 !== 'NA'
                                ? `/product/${product.design}/${product.tech1}/${product.tech2}/`
                                : `/product/${product.design}/${product.tech1}/`
                        }
                    >{product?.name}</a>
                </h5>
                <p className="text-gray-500 dark:text-gray-300 font-normal text-sm md:text-base mb-3">
                    ${product?.price}
                </p>
            </div>
            <div className="hidden md:block w-px h-auto bg-gray-300"></div>
            <div className="basis-1/2">
                <div className="flex items-center justify-center flex-col">
                    <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-3">Buy Hosting - provided by HOSTINGER</h2>
                    <img className="w-36 h-36" src="https://d7h9v39iheghu.cloudfront.net/previews/da691f97-99cf-45a2-885d-1e5357ee3d49/27aa7cc1-3892-429c-990f-12c38282097e/27aa7cc1-3892-429c-990f-12c38282097e/1952x1000.jpg?Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDdoOXYzOWloZWdodS5jbG91ZGZyb250Lm5ldC9wcmV2aWV3cy9kYTY5MWY5Ny05OWNmLTQ1YTItODg1ZC0xZTUzNTdlZTNkNDkqIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzYwMTUxNjI4fX19XX0_&Signature=BwDcv4YnkrJMXXqNlsq0q3Ax-nPoEtEf9ckfnvvEs4pb24kFkv6Hl6A-B~BmLREF~AwrxxGyt7-6mVTGnEIf8CNs4cpZYRfIO8fUdcO0CzqJ9pkxmIFAhKlUcUZ0xbK7ntzw82tgI4SrIjTuwlo8Xn3wmTtCiLcFo3irEKeoPtlwuRS4eKJLEOh~U59bHTiucKZ6mVZX6Rxrp983jXGtogf6WfL6BWTbP3vKhquT37jwaH9UV7GMsjLNdVEZ60IjxN1QIssLou4McmYb0ZND5bnHw~wY8GU00VsNUmOispiztDQa0JM37QNhbUB8Of94yKJMF2RwmCCGfPkKP0disA__&Key-Pair-Id=APKAJXJN6VNR3OLZJXJA" alt="" />
                </div>
            </div>
        </section>
    )
}

export default CardPopup;