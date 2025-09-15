import React from 'react';
import { Button, Modal } from "flowbite-react";

const baseURL = window.location.origin;

export function Status({ open, handleClose, status, isError }) {
    return (
        <>
            <Modal show={open} onClose={handleClose}>
                <Modal.Header>Status</Modal.Header>
                <Modal.Body>
                    <div className="">
                        <span className="block text-base leading-relaxed text-gray-500 dark:text-gray-400">
                            <b>Status:</b> {status?.status}
                        </span>
                        <span className="block text-base leading-relaxed text-gray-500 dark:text-gray-400">
                            <b>Info:</b> {status?.info}
                        </span>
                    </div>
                </Modal.Body>
                <Modal.Footer>
                    {!isError ? (
                        <>
                            {(status?.gh_repo || status?.download_link) && (
                                <center>
                                    {status?.gh_repo && (
                                        <>
                                            Access the{' '}
                                            <a href={status.gh_repo} target="_blank" rel="noopener noreferrer">
                                                Generated Repository
                                            </a>
                                        </>
                                    )}

                                    {status?.gh_repo && status?.download_link && ' or '}

                                    {status?.download_link && (
                                        <>
                                            download the{' '}
                                            <a href={status.download_link} download>
                                                ZIP Archive
                                            </a>
                                        </>
                                    )}
                                </center>
                            )}
                        </>
                    ) : (
                        <center>
                            For assistance please contact{' '}
                            <a href={`${baseURL}/ticket/create/`}
                                target="_blank"
                                rel="django-generator"
                            >
                                support
                            </a>
                        </center>
                    )}
                </Modal.Footer>
                {!isError &&
                <Modal.Footer>
                    <div className='w-full flex justify-center items-center flex-col'>
                        <p className='mb-2 text-center'>
                            <a className='text-gray-600 dark:text-gray-200' href="">Get Hosting - 2.99/mo</a>
                        </p>
                        <a className='text-center' href="#">
                            <img 
                                className='w-16 h-14'
                                src="https://d7h9v39iheghu.cloudfront.net/previews/da691f97-99cf-45a2-885d-1e5357ee3d49/3dddef1b-88fb-4f8d-9466-4de63fb3cc5d/3dddef1b-88fb-4f8d-9466-4de63fb3cc5d/1952x1000.jpg?Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDdoOXYzOWloZWdodS5jbG91ZGZyb250Lm5ldC9wcmV2aWV3cy9kYTY5MWY5Ny05OWNmLTQ1YTItODg1ZC0xZTUzNTdlZTNkNDkqIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzYwNDk5OTIzfX19XX0_&Signature=Sr9DFt4X2uMk6I1BLWRU8zZqIQxtPRSLXq15uUxs6uSPTTC0k-XkcDI7NTl7Sm~g68qm1u2jBNALTRnEHXJr-5LoEM8TwdnJ0sLts8BF8XEY7hlrQdeNxOGGZ5j0ViKRtdGssJLoFYkyqbRNhcl5l5t0UldNAudBG77MK~QIt~mN5SSNdky3HasJI6WXY7gH7KLfBcZkh9H7SiQzjJY0WAS6ZJqX8iPuzAhOToU6sVdymhj-81RW5RIKOTdU-LY3TVxMjEPvc~FANrR6UxKg9QHydkat3fdEA7SUHtS2U3XQxycr-XjLhgVZdYcfGQEdq~6tK55KOWXS0dvq4-Wiww__&Key-Pair-Id=APKAJXJN6VNR3OLZJXJA" alt="" />
                        </a>
                    </div>
                </Modal.Footer>}
            </Modal>
        </>
    );
}
