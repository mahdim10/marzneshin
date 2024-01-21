
import {
    Box,
    chakra,
    ChakraComponent,
    Flex,
    Spacer,
    Stack,
    Text,
} from "@chakra-ui/react";
import { ServerStackIcon, UsersIcon } from "@heroicons/react/24/outline";
import {
    useDashboard,
} from "contexts/DashboardContext";
import { FC, forwardRef, PropsWithChildren, useEffect, useState } from "react";
import {
    useFormContext,
} from "react-hook-form";
import { Service } from "types/Service";

const ServiceIconBaseStyle = {
    baseStyle: {
        strokeWidth: "2px",
        color: "primary.500",
        w: 5,
        h: 5,
        mx: "6px",
    },
}

const UsersServiceIcon = chakra(UsersIcon, ServiceIconBaseStyle);

const InboundsServiceIcon = chakra(ServerStackIcon, ServiceIconBaseStyle);

type ServicePropertyStatusProps = {
    value: number;
    StatusIcon: ChakraComponent;
}

const ServicePropertyStatus: FC<ServicePropertyStatusProps> = ({ value, StatusIcon }) => {
    const [valueState, _] = useState(value);
    return (
        <Flex flexDirection="row">
            <StatusIcon />
            <span>{valueState}</span>
        </Flex>
    );
};

type CustomCheckboxProps = {
    isChecked: boolean;
    onChange: () => void;
    service: Service;
    value: string;
}

const CustomCheckbox = forwardRef(
    ({ isChecked, onChange, service, ...props }: CustomCheckboxProps, ref: Ref<HTMLDivElement>) => (
        <Box
            ref={ref}
            border={isChecked ? '5px' : '2px'}
            w="full"
            borderColor={isChecked ? 'primary.500' : 'gray.600'}
            boxShadow={isChecked ? "0 0 0 3px rgba(102, 126, 234, 0.6)" : "0 0 0 1px rgba(102, 126, 234, 0.6)"}
            bg={isChecked ? 'gray.100' : 'white'}
            py="4px"
            px="8px"
            borderRadius="md"
            display="flex"
            alignItems="center"
            justifyContent="center"
            _hover={{
                cursor: 'pointer',
                borderColor: 'primary.300',
            }}
            onClick={onChange}
            {...props}
        >
            <Text fontSize="sm" color="gray.700" fontWeight="medium">
                {service.name}
            </Text>
            <Spacer />
            <Flex flexDirection="row" alignItems="center">
                <ServicePropertyStatus value={service.users.length} StatusIcon={UsersServiceIcon} />
                <Text color="primary.600" mx="8px">/</Text>
                <ServicePropertyStatus value={service.inbounds.length} StatusIcon={InboundsServiceIcon} />
            </Flex>
        </Box>
    )
);


interface ServicesSelectListProps {
    list: Service[];
}

export const ServicesSelectList = forwardRef<HTMLDivElement, ServicesSelectListProps>(
    function({ list, ...props }, ref) {
        const form = useFormContext();

        const handleServiceToggle = (serviceId: number) => {
            const currentServices = form.getValues('services');
            const isSelected = currentServices.includes(serviceId);

            let updatedServices;

            if (isSelected) {
                updatedServices = currentServices.filter((id: number) => id !== serviceId);
            } else {
                updatedServices = [...currentServices, serviceId];
            }

            form.setValue('services', updatedServices, { shouldValidate: true });
        };

        return (
            <Stack spacing={3} ref={ref}>
                {list.map((service: Service) => (
                    <Box key={service.id}>
                        <Flex align="center">
                            <CustomCheckbox
                                isChecked={form.getValues('services').includes(service.id)}
                                onChange={() => handleServiceToggle(service.id)}
                                service={service}
                                value={String(service.id)}
                            />
                        </Flex>
                    </Box>
                ))}
            </Stack>
        );
    });
