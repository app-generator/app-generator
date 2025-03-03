import React from 'react';
import { Button, Modal } from "flowbite-react";

export function ProModal({ open, handleClose, price }) {
    return (
        <>
            <Modal
                show={open}
                onClose={handleClose}
                size='4xl'
            >
                <Modal.Header>Pro Subscription</Modal.Header>
                <Modal.Body>
                    <div id="pro-subscription" className="mb-5 border border-gray-200 p-5 rounded-lg flex items-center gap-16">
                        <div className="basis-3/5">
                            <h4 className="text-gray-900 dark:text-white font-bold text-xl mb-3">Pro Subscription</h4>
                            <p className="text-gray-500 dark:text-gray-300 mb-5">
                                Here are the benefits:
                            </p>

                            <div className="flex flex-col gap-3 md:gap-3 mb-3">
                                <div className="flex items-start gap-2">
                                    <div className="bg-primary-100 rounded-full p-0.5">
                                        <svg className="w-5 h-5 text-primary-700" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                            <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 11.917 9.724 16.5 19 7.5" />
                                        </svg>
                                    </div>
                                    <p className="text-gray-500 dark:text-gray-300 text-sm md:text-base">
                                        <span className="text-gray-900 dark:text-white">
                                            <a target="_blank" href="/onboarding-kit/">Onboarding Kit</a>{' - '}
                                        </span>Premium Dashboards, Dynamic Django Tool, and eCommerce CMS included - <a target="_blank" href="/onboarding-kit/">See Details</a>.
                                    </p>
                                </div>
                            </div>

                            <div className="flex flex-col gap-3 md:gap-3 mb-3">
                                <div className="flex items-start gap-2">
                                    <div className="bg-primary-100 rounded-full p-0.5">
                                        <svg className="w-5 h-5 text-primary-700" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                            <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 11.917 9.724 16.5 19 7.5" />
                                        </svg>
                                    </div>
                                    <p className="text-gray-500 dark:text-gray-300 text-sm md:text-base">
                                        <span className="text-gray-900 dark:text-white font-bold">
                                            Unlock a New Premium Starter at each 4mo
                                        </span> (Personal License) - <a target="_blank" href="/product/?search=pro">See List</a>.
                                    </p>
                                </div>
                            </div>

                            <div className="flex flex-col gap-3 md:gap-3 mb-3">
                                <div className="flex items-start gap-2">
                                    <div className="bg-primary-100 rounded-full p-0.5">
                                        <svg className="w-5 h-5 text-primary-700" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                            <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 11.917 9.724 16.5 19 7.5" />
                                        </svg>
                                    </div>
                                    <p className="text-gray-500 dark:text-gray-300 text-sm md:text-base">
                                        <span className="text-gray-900 dark:text-white font-bold">
                                            Premium Support
                                        </span>{' - '}Monday-Sunday, 3h response time.
                                    </p>
                                </div>
                            </div>

                            <div className="flex flex-col gap-3 md:gap-3 mb-3">
                                <div className="flex items-start gap-2">
                                    <div className="bg-primary-100 rounded-full p-0.5">
                                        <svg className="w-5 h-5 text-primary-700" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                            <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 11.917 9.724 16.5 19 7.5" />
                                        </svg>
                                    </div>
                                    <p className="text-gray-500 dark:text-gray-300 text-sm md:text-base">
                                        <span className="text-gray-900 dark:text-white">
                                            <a target="_blank" href="/tools/django-generator/">Django Generator</a>{' - '}
                                        </span>Unlimited starters, all features available.
                                    </p>
                                </div>
                            </div>

                            <div className="flex flex-col gap-3 md:gap-3 mb-3">
                                <div className="flex items-start gap-2">
                                    <div className="bg-primary-100 rounded-full p-0.5">
                                        <svg className="w-5 h-5 text-primary-700" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                            <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 11.917 9.724 16.5 19 7.5" />
                                        </svg>
                                    </div>
                                    <p className="text-gray-500 dark:text-gray-300 text-sm md:text-base">
                                        <span className="text-gray-900 dark:text-white">
                                            <a target="_blank" href="/tools/flask-generator/">Flask Generator</a>{' - '}
                                        </span>Unlimited starters, all features available.
                                    </p>
                                </div>
                            </div>                            

                            <div className="flex flex-col gap-3 md:gap-3 mb-3">
                                <div className="flex items-start gap-2">
                                    <div className="bg-primary-100 rounded-full p-0.5">
                                        <svg className="w-5 h-5 text-primary-700" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                            <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 11.917 9.724 16.5 19 7.5" />
                                        </svg>
                                    </div>
                                    <p className="text-gray-500 dark:text-gray-300 text-sm md:text-base">
                                        <span className="text-gray-900 dark:text-white">
                                            <a target="_blank" href="/tools/csv-processor/">CSV Processor</a>{' - '}
                                        </span>Full Access (all features).
                                    </p>
                                </div>
                            </div>

                            <div className="flex flex-col gap-3 md:gap-3 mb-3">
                                <div className="flex items-start gap-2">
                                    <div className="bg-primary-100 rounded-full p-0.5">
                                        <svg className="w-5 h-5 text-primary-700" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                            <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 11.917 9.724 16.5 19 7.5" />
                                        </svg>
                                    </div>
                                    <p className="text-gray-500 dark:text-gray-300 text-sm md:text-base">
                                        <span className="text-gray-900 dark:text-white">
                                            <a target="_blank" href="/tools/db-migrator/">DataBase Migrator</a>{' - '}
                                        </span>Full access (all features).
                                    </p>
                                </div>
                            </div>

                            <div className="flex flex-col gap-3 md:gap-3">
                                <div className="flex items-start gap-2">
                                    <div className="bg-primary-100 rounded-full p-0.5">
                                        <svg className="w-5 h-5 text-primary-700" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                            <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 11.917 9.724 16.5 19 7.5" />
                                        </svg>
                                    </div>
                                    <p className="text-gray-500 dark:text-gray-300 text-sm md:text-base">
                                        <span className="text-gray-900 dark:text-white">
                                            <a target="_blank" href="/tools/db-processor/">DataBase Processor</a>{' - '}
                                        </span>Full Access (all features).
                                    </p>
                                </div>
                            </div>

                        </div>
                        <div className="hidden md:block w-px self-stretch bg-gray-300"></div>
                        <div className="basis-1/5 w-full flex flex-col items-center ">
                            <div className="mb-5 text-center w-full">
                                <h2 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-3">
                                    ${price}/mo
                                </h2>
                                <p className="text-gray-500 dark:text-gray-300 text-xs md:text-sm">Monthly subscription (cancel anytime)</p>
                            </div>
                            <a target="_blank" href="https://appseed.gumroad.com/l/pro-subscription" className="mb-5 text-white w-full inline-flex items-center justify-center bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                                Subscribe
                                <svg className="w-5 h-5 text-white ml-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                    <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 12H5m14 0-4 4m4-4-4-4" />
                                </svg>
                            </a>
                            <div className="text-center w-full">
                                <p className="text-gray-500 dark:text-gray-300 text-xs md:text-sm">
                                    Payment Secured by</p>
                                <img className="block mx-auto" src="/static/dist/img/gumroad.png" alt="GUMROAD Image" />
                            </div>
                        </div>
                    </div>
                </Modal.Body>
            </Modal>
        </>
    );
}
