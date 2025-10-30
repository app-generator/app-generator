import React, { useEffect, useState } from 'react';
import { Button, Modal, ModalBody, ModalHeader, Textarea } from "flowbite-react";
import axios from 'axios';
import GumroadLink from './GumroadLink';

const CardPopup = ({ productId, baseURL, isAuthenticated }) => {
    const [product, setProduct] = useState({});
    const [openModal, setOpenModal] = useState(false);
    const promoCode = '/BOOST_2025'

    function onCloseModal() {
        setOpenModal(false);
    }

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
        <section className="border border-gray-600 dark:border-gray-200 rounded-lg p-3 md:p-8 flex justify-between gap-10 shadow-md flex-col md:flex-row">
            <div className="basis-1/2">
                <p className='mb-5 text-center dark:text-gray-200'>{product.info}</p>
                <div className="flex items-center justify-center gap-2 flex-wrap">
                    <a target="_blank" href={product.demo_url} className="inline-flex items-center gap-2 py-2.5 px-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">
                        Live Demo                   
                    </a>
                    <GumroadLink payUrl={product.pay_url} promoCode={promoCode}>
                        Purchase - ${product.price}
                    </GumroadLink>
                </div>
            </div>
            <div className="hidden md:block w-px h-auto bg-gray-300"></div>
            <div className="basis-1/2">
                <div className="flex items-center justify-center flex-col">
                    <h2 className="text-base font-bold text-gray-900 dark:text-white mb-3">
                        <a target='_blank' className="text-primary-500 underline" href="https://www.hostg.xyz/aff_c?offer_id=6&aff_id=207452">Buy Hosting</a> - $2.99/mo
                    </h2>
                    Provided by
                    <a target='_blank' href="https://www.hostg.xyz/aff_c?offer_id=6&aff_id=207452">
                        HOSTINGER
                    </a>
                </div>
            </div>
            <div className="hidden md:block w-px h-auto bg-gray-300"></div>
            <div className="basis-1/2">
                <div className="flex items-center justify-center flex-col">
                    <h2 className="text-center text-base font-bold text-gray-900 dark:text-white mb-3">Custom Development</h2>
                    <p className='text-center text-sm mb-3 dark:text-gray-200'>Customize your product or build an MVP in record time</p>
                    <button 
                        onClick={() => setOpenModal(true)}
                        type='button'
                        className="inline-flex items-center gap-2 text-white bg-blue-700 hover:bg-blue-800 hover:text-white focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-3 py-2.5 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
                        Contact Support
                    </button>
                </div>
            </div>


            <Modal show={openModal} size="xl" onClose={onCloseModal} popup>
                <ModalHeader />
                <ModalBody>
                    <div className="space-y-6">
                        {isAuthenticated ? (
                            <>
                                <div>
                                    <h2 className="text-base font-bold text-gray-900 dark:text-white mb-3">Custom develoment request</h2>
                                    <Textarea id="message" placeholder='Tell us more about your product' required />
                                </div>
                                <div className="w-full">
                                    <Button className='w-full' color='dark'>Submit</Button>
                                </div>
                            </>
                        ) : (
                            <>
                            <h2 className="text-base font-bold text-gray-900 dark:text-white mb-3">Action reserved for authenticated users</h2>
                            <div className="w-full">
                                <Button onClick={() => window.location.href = "/users/signin/"} color='dark'>Signin</Button>
                            </div>
                            </>
                        )}
                    </div>
                </ModalBody>
            </Modal>

        </section>
    )
}

export default CardPopup;