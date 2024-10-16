import {
    Page,
    Loading,
} from '@marzneshin/components';
import { UsersNoServiceAlert, UsersTable } from '@marzneshin/modules/users';
import { createFileRoute, Outlet } from '@tanstack/react-router'
import { type FC, Suspense } from 'react';
import { useTranslation } from 'react-i18next';

export const UsersPage: FC = () => {
    const { t } = useTranslation();

    return (
        <Page
            title={t('users')}
            footer={
                <UsersNoServiceAlert />
            }
        >
            <UsersTable />
            <Suspense fallback={<Loading />}>
                <Outlet />
            </Suspense>
        </Page>
    )
};

export const Route = createFileRoute('/_dashboard/users')({
    component: () => <UsersPage />,
})
