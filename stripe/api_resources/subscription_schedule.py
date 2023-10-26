# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from stripe.util import class_method_variant
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.application import Application
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.subscription import Subscription
    from stripe.api_resources.test_helpers.test_clock import TestClock


class SubscriptionSchedule(
    CreateableAPIResource["SubscriptionSchedule"],
    ListableAPIResource["SubscriptionSchedule"],
    UpdateableAPIResource["SubscriptionSchedule"],
):
    """
    A subscription schedule allows you to create and manage the lifecycle of a subscription by predefining expected changes.

    Related guide: [Subscription schedules](https://stripe.com/docs/billing/subscriptions/subscription-schedules)
    """

    OBJECT_NAME: ClassVar[
        Literal["subscription_schedule"]
    ] = "subscription_schedule"
    if TYPE_CHECKING:

        class CancelParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            invoice_now: NotRequired["bool|None"]
            """
            If the subscription schedule is `active`, indicates if a final invoice will be generated that contains any un-invoiced metered usage and new/pending proration invoice items. Defaults to `true`.
            """
            prorate: NotRequired["bool|None"]
            """
            If the subscription schedule is `active`, indicates if the cancellation should be prorated. Defaults to `true`.
            """

        class CreateParams(RequestOptions):
            customer: NotRequired["str|None"]
            """
            The identifier of the customer to create the subscription schedule for.
            """
            default_settings: NotRequired[
                "SubscriptionSchedule.CreateParamsDefaultSettings|None"
            ]
            """
            Object representing the subscription schedule's default settings.
            """
            end_behavior: NotRequired[
                "Literal['cancel', 'none', 'release', 'renew']|None"
            ]
            """
            Behavior of the subscription schedule and underlying subscription when it ends. Possible values are `release` or `cancel` with the default being `release`. `release` will end the subscription schedule and keep the underlying subscription running.`cancel` will end the subscription schedule and cancel the underlying subscription.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            from_subscription: NotRequired["str|None"]
            """
            Migrate an existing subscription to be managed by a subscription schedule. If this parameter is set, a subscription schedule will be created using the subscription's item(s), set to auto-renew using the subscription's interval. When using this parameter, other parameters (such as phase values) cannot be set. To create a subscription schedule with other modifications, we recommend making two separate API calls.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            phases: NotRequired[
                "List[SubscriptionSchedule.CreateParamsPhase]|None"
            ]
            """
            List representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, the `end_date` of one phase will always equal the `start_date` of the next phase.
            """
            start_date: NotRequired["int|Literal['now']|None"]
            """
            When the subscription schedule starts. We recommend using `now` so that it starts the subscription immediately. You can also use a Unix timestamp to backdate the subscription so that it starts on a past date, or set a future date for the subscription to start on.
            """

        class CreateParamsPhase(TypedDict):
            add_invoice_items: NotRequired[
                "List[SubscriptionSchedule.CreateParamsPhaseAddInvoiceItem]|None"
            ]
            """
            A list of prices and quantities that will generate invoice items appended to the next invoice for this phase. You may pass up to 20 items.
            """
            application_fee_percent: NotRequired["float|None"]
            """
            A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
            """
            automatic_tax: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseAutomaticTax|None"
            ]
            """
            Automatic tax settings for this phase.
            """
            billing_cycle_anchor: NotRequired[
                "Literal['automatic', 'phase_start']|None"
            ]
            """
            Can be set to `phase_start` to set the anchor to the start of the phase or `automatic` to automatically change it if needed. Cannot be set to `phase_start` if this phase specifies a trial. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
            """
            billing_thresholds: NotRequired[
                "Literal['']|SubscriptionSchedule.CreateParamsPhaseBillingThresholds|None"
            ]
            """
            Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds.
            """
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            """
            Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically` on creation.
            """
            coupon: NotRequired["str|None"]
            """
            The identifier of the coupon to apply to this phase of the subscription schedule.
            """
            currency: NotRequired["str|None"]
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            default_payment_method: NotRequired["str|None"]
            """
            ID of the default payment method for the subscription schedule. It must belong to the customer associated with the subscription schedule. If not set, invoices will use the default payment method in the customer's invoice settings.
            """
            default_tax_rates: NotRequired["Literal['']|List[str]|None"]
            """
            A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will set the Subscription's [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates), which means they will be the Invoice's [`default_tax_rates`](https://stripe.com/docs/api/invoices/create#create_invoice-default_tax_rates) for any Invoices issued by the Subscription during this Phase.
            """
            description: NotRequired["Literal['']|str|None"]
            """
            Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription.
            """
            end_date: NotRequired["int|None"]
            """
            The date at which this phase of the subscription schedule ends. If set, `iterations` must not be set.
            """
            invoice_settings: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseInvoiceSettings|None"
            ]
            """
            All invoices will be billed using the specified settings.
            """
            items: List["SubscriptionSchedule.CreateParamsPhaseItem"]
            """
            List of configuration items, each with an attached price, to apply during this phase of the subscription schedule.
            """
            iterations: NotRequired["int|None"]
            """
            Integer representing the multiplier applied to the price interval. For example, `iterations=2` applied to a price with `interval=month` and `interval_count=3` results in a phase of duration `2 * 3 months = 6 months`. If set, `end_date` must not be set.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to a phase. Metadata on a schedule's phase will update the underlying subscription's `metadata` when the phase is entered, adding new keys and replacing existing keys in the subscription's `metadata`. Individual keys in the subscription's `metadata` can be unset by posting an empty value to them in the phase's `metadata`. To unset all keys in the subscription's `metadata`, update the subscription directly or unset every key individually from the phase's `metadata`.
            """
            on_behalf_of: NotRequired["str|None"]
            """
            The account on behalf of which to charge, for each of the associated subscription's invoices.
            """
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            """
            Whether the subscription schedule will create [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when transitioning to this phase. The default value is `create_prorations`. This setting controls prorations when a phase is started asynchronously and it is persisted as a field on the phase. It's different from the request-level [proration_behavior](https://stripe.com/docs/api/subscription_schedules/update#update_subscription_schedule-proration_behavior) parameter which controls what happens if the update request affects the billing configuration of the current phase.
            """
            transfer_data: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseTransferData|None"
            ]
            """
            The data with which to automatically create a Transfer for each of the associated subscription's invoices.
            """
            trial: NotRequired["bool|None"]
            """
            If set to true the entire phase is counted as a trial and the customer will not be charged for any fees.
            """
            trial_end: NotRequired["int|None"]
            """
            Sets the phase to trialing from the start date to this date. Must be before the phase end date, can not be combined with `trial`
            """

        class CreateParamsPhaseTransferData(TypedDict):
            amount_percent: NotRequired["float|None"]
            """
            A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination.
            """
            destination: str
            """
            ID of an existing, connected Stripe account.
            """

        class CreateParamsPhaseItem(TypedDict):
            billing_thresholds: NotRequired[
                "Literal['']|SubscriptionSchedule.CreateParamsPhaseItemBillingThresholds|None"
            ]
            """
            Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to a configuration item. Metadata on a configuration item will update the underlying subscription item's `metadata` when the phase is entered, adding new keys and replacing existing keys. Individual keys in the subscription item's `metadata` can be unset by posting an empty value to them in the configuration item's `metadata`. To unset all keys in the subscription item's `metadata`, update the subscription item directly or unset every key individually from the configuration item's `metadata`.
            """
            plan: NotRequired["str|None"]
            """
            The plan ID to subscribe to. You may specify the same ID in `plan` and `price`.
            """
            price: NotRequired["str|None"]
            """
            The ID of the price object.
            """
            price_data: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseItemPriceData|None"
            ]
            """
            Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
            """
            quantity: NotRequired["int|None"]
            """
            Quantity for the given price. Can be set only if the price's `usage_type` is `licensed` and not `metered`.
            """
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            """
            A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will override the [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates.
            """

        class CreateParamsPhaseItemPriceData(TypedDict):
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            product: str
            """
            The ID of the product that this price will belong to.
            """
            recurring: "SubscriptionSchedule.CreateParamsPhaseItemPriceDataRecurring"
            """
            The recurring components of a price such as `interval` and `interval_count`.
            """
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            """
            Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
            """
            unit_amount: NotRequired["int|None"]
            """
            A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
            """
            unit_amount_decimal: NotRequired["str|None"]
            """
            Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
            """

        class CreateParamsPhaseItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            """
            Specifies billing frequency. Either `day`, `week`, `month` or `year`.
            """
            interval_count: NotRequired["int|None"]
            """
            The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks).
            """

        class CreateParamsPhaseItemBillingThresholds(TypedDict):
            usage_gte: int
            """
            Number of units that meets the billing threshold to advance the subscription to a new billing period (e.g., it takes 10 $5 units to meet a $50 [monetary threshold](https://stripe.com/docs/api/subscriptions/update#update_subscription-billing_thresholds-amount_gte))
            """

        class CreateParamsPhaseInvoiceSettings(TypedDict):
            days_until_due: NotRequired["int|None"]
            """
            Number of days within which a customer must pay invoices generated by this subscription schedule. This value will be `null` for subscription schedules where `billing=charge_automatically`.
            """

        class CreateParamsPhaseBillingThresholds(TypedDict):
            amount_gte: NotRequired["int|None"]
            """
            Monetary threshold that triggers the subscription to advance to a new billing period
            """
            reset_billing_cycle_anchor: NotRequired["bool|None"]
            """
            Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged.
            """

        class CreateParamsPhaseAutomaticTax(TypedDict):
            enabled: bool
            """
            Enabled automatic tax calculation which will automatically compute tax rates on all invoices generated by the subscription.
            """

        class CreateParamsPhaseAddInvoiceItem(TypedDict):
            price: NotRequired["str|None"]
            """
            The ID of the price object.
            """
            price_data: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseAddInvoiceItemPriceData|None"
            ]
            """
            Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
            """
            quantity: NotRequired["int|None"]
            """
            Quantity for this item. Defaults to 1.
            """
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            """
            The tax rates which apply to the item. When set, the `default_tax_rates` do not apply to this item.
            """

        class CreateParamsPhaseAddInvoiceItemPriceData(TypedDict):
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            product: str
            """
            The ID of the product that this price will belong to.
            """
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            """
            Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
            """
            unit_amount: NotRequired["int|None"]
            """
            A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
            """
            unit_amount_decimal: NotRequired["str|None"]
            """
            Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
            """

        class CreateParamsDefaultSettings(TypedDict):
            application_fee_percent: NotRequired["float|None"]
            """
            A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
            """
            automatic_tax: NotRequired[
                "SubscriptionSchedule.CreateParamsDefaultSettingsAutomaticTax|None"
            ]
            """
            Default settings for automatic tax computation.
            """
            billing_cycle_anchor: NotRequired[
                "Literal['automatic', 'phase_start']|None"
            ]
            """
            Can be set to `phase_start` to set the anchor to the start of the phase or `automatic` to automatically change it if needed. Cannot be set to `phase_start` if this phase specifies a trial. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
            """
            billing_thresholds: NotRequired[
                "Literal['']|SubscriptionSchedule.CreateParamsDefaultSettingsBillingThresholds|None"
            ]
            """
            Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds.
            """
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            """
            Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically` on creation.
            """
            default_payment_method: NotRequired["str|None"]
            """
            ID of the default payment method for the subscription schedule. It must belong to the customer associated with the subscription schedule. If not set, invoices will use the default payment method in the customer's invoice settings.
            """
            description: NotRequired["Literal['']|str|None"]
            """
            Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription.
            """
            invoice_settings: NotRequired[
                "SubscriptionSchedule.CreateParamsDefaultSettingsInvoiceSettings|None"
            ]
            """
            All invoices will be billed using the specified settings.
            """
            on_behalf_of: NotRequired["Literal['']|str|None"]
            """
            The account on behalf of which to charge, for each of the associated subscription's invoices.
            """
            transfer_data: NotRequired[
                "Literal['']|SubscriptionSchedule.CreateParamsDefaultSettingsTransferData|None"
            ]
            """
            The data with which to automatically create a Transfer for each of the associated subscription's invoices.
            """

        class CreateParamsDefaultSettingsTransferData(TypedDict):
            amount_percent: NotRequired["float|None"]
            """
            A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination.
            """
            destination: str
            """
            ID of an existing, connected Stripe account.
            """

        class CreateParamsDefaultSettingsInvoiceSettings(TypedDict):
            days_until_due: NotRequired["int|None"]
            """
            Number of days within which a customer must pay invoices generated by this subscription schedule. This value will be `null` for subscription schedules where `collection_method=charge_automatically`.
            """

        class CreateParamsDefaultSettingsBillingThresholds(TypedDict):
            amount_gte: NotRequired["int|None"]
            """
            Monetary threshold that triggers the subscription to advance to a new billing period
            """
            reset_billing_cycle_anchor: NotRequired["bool|None"]
            """
            Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged.
            """

        class CreateParamsDefaultSettingsAutomaticTax(TypedDict):
            enabled: bool
            """
            Enabled automatic tax calculation which will automatically compute tax rates on all invoices generated by the subscription.
            """

        class ListParams(RequestOptions):
            canceled_at: NotRequired[
                "SubscriptionSchedule.ListParamsCanceledAt|int|None"
            ]
            """
            Only return subscription schedules that were created canceled the given date interval.
            """
            completed_at: NotRequired[
                "SubscriptionSchedule.ListParamsCompletedAt|int|None"
            ]
            """
            Only return subscription schedules that completed during the given date interval.
            """
            created: NotRequired[
                "SubscriptionSchedule.ListParamsCreated|int|None"
            ]
            """
            Only return subscription schedules that were created during the given date interval.
            """
            customer: NotRequired["str|None"]
            """
            Only return subscription schedules for the given customer.
            """
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            released_at: NotRequired[
                "SubscriptionSchedule.ListParamsReleasedAt|int|None"
            ]
            """
            Only return subscription schedules that were released during the given date interval.
            """
            scheduled: NotRequired["bool|None"]
            """
            Only return subscription schedules that have not started yet.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """

        class ListParamsReleasedAt(TypedDict):
            gt: NotRequired["int|None"]
            """
            Minimum value to filter by (exclusive)
            """
            gte: NotRequired["int|None"]
            """
            Minimum value to filter by (inclusive)
            """
            lt: NotRequired["int|None"]
            """
            Maximum value to filter by (exclusive)
            """
            lte: NotRequired["int|None"]
            """
            Maximum value to filter by (inclusive)
            """

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            """
            Minimum value to filter by (exclusive)
            """
            gte: NotRequired["int|None"]
            """
            Minimum value to filter by (inclusive)
            """
            lt: NotRequired["int|None"]
            """
            Maximum value to filter by (exclusive)
            """
            lte: NotRequired["int|None"]
            """
            Maximum value to filter by (inclusive)
            """

        class ListParamsCompletedAt(TypedDict):
            gt: NotRequired["int|None"]
            """
            Minimum value to filter by (exclusive)
            """
            gte: NotRequired["int|None"]
            """
            Minimum value to filter by (inclusive)
            """
            lt: NotRequired["int|None"]
            """
            Maximum value to filter by (exclusive)
            """
            lte: NotRequired["int|None"]
            """
            Maximum value to filter by (inclusive)
            """

        class ListParamsCanceledAt(TypedDict):
            gt: NotRequired["int|None"]
            """
            Minimum value to filter by (exclusive)
            """
            gte: NotRequired["int|None"]
            """
            Minimum value to filter by (inclusive)
            """
            lt: NotRequired["int|None"]
            """
            Maximum value to filter by (exclusive)
            """
            lte: NotRequired["int|None"]
            """
            Maximum value to filter by (inclusive)
            """

        class ModifyParams(RequestOptions):
            default_settings: NotRequired[
                "SubscriptionSchedule.ModifyParamsDefaultSettings|None"
            ]
            """
            Object representing the subscription schedule's default settings.
            """
            end_behavior: NotRequired[
                "Literal['cancel', 'none', 'release', 'renew']|None"
            ]
            """
            Behavior of the subscription schedule and underlying subscription when it ends. Possible values are `release` or `cancel` with the default being `release`. `release` will end the subscription schedule and keep the underlying subscription running.`cancel` will end the subscription schedule and cancel the underlying subscription.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            phases: NotRequired[
                "List[SubscriptionSchedule.ModifyParamsPhase]|None"
            ]
            """
            List representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, the `end_date` of one phase will always equal the `start_date` of the next phase. Note that past phases can be omitted.
            """
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            """
            If the update changes the current phase, indicates whether the changes should be prorated. The default value is `create_prorations`.
            """

        class ModifyParamsPhase(TypedDict):
            add_invoice_items: NotRequired[
                "List[SubscriptionSchedule.ModifyParamsPhaseAddInvoiceItem]|None"
            ]
            """
            A list of prices and quantities that will generate invoice items appended to the next invoice for this phase. You may pass up to 20 items.
            """
            application_fee_percent: NotRequired["float|None"]
            """
            A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
            """
            automatic_tax: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseAutomaticTax|None"
            ]
            """
            Automatic tax settings for this phase.
            """
            billing_cycle_anchor: NotRequired[
                "Literal['automatic', 'phase_start']|None"
            ]
            """
            Can be set to `phase_start` to set the anchor to the start of the phase or `automatic` to automatically change it if needed. Cannot be set to `phase_start` if this phase specifies a trial. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
            """
            billing_thresholds: NotRequired[
                "Literal['']|SubscriptionSchedule.ModifyParamsPhaseBillingThresholds|None"
            ]
            """
            Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds.
            """
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            """
            Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically` on creation.
            """
            coupon: NotRequired["str|None"]
            """
            The identifier of the coupon to apply to this phase of the subscription schedule.
            """
            currency: NotRequired["str|None"]
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            default_payment_method: NotRequired["str|None"]
            """
            ID of the default payment method for the subscription schedule. It must belong to the customer associated with the subscription schedule. If not set, invoices will use the default payment method in the customer's invoice settings.
            """
            default_tax_rates: NotRequired["Literal['']|List[str]|None"]
            """
            A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will set the Subscription's [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates), which means they will be the Invoice's [`default_tax_rates`](https://stripe.com/docs/api/invoices/create#create_invoice-default_tax_rates) for any Invoices issued by the Subscription during this Phase.
            """
            description: NotRequired["Literal['']|str|None"]
            """
            Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription.
            """
            end_date: NotRequired["int|Literal['now']|None"]
            """
            The date at which this phase of the subscription schedule ends. If set, `iterations` must not be set.
            """
            invoice_settings: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseInvoiceSettings|None"
            ]
            """
            All invoices will be billed using the specified settings.
            """
            items: List["SubscriptionSchedule.ModifyParamsPhaseItem"]
            """
            List of configuration items, each with an attached price, to apply during this phase of the subscription schedule.
            """
            iterations: NotRequired["int|None"]
            """
            Integer representing the multiplier applied to the price interval. For example, `iterations=2` applied to a price with `interval=month` and `interval_count=3` results in a phase of duration `2 * 3 months = 6 months`. If set, `end_date` must not be set.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to a phase. Metadata on a schedule's phase will update the underlying subscription's `metadata` when the phase is entered, adding new keys and replacing existing keys in the subscription's `metadata`. Individual keys in the subscription's `metadata` can be unset by posting an empty value to them in the phase's `metadata`. To unset all keys in the subscription's `metadata`, update the subscription directly or unset every key individually from the phase's `metadata`.
            """
            on_behalf_of: NotRequired["str|None"]
            """
            The account on behalf of which to charge, for each of the associated subscription's invoices.
            """
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            """
            Whether the subscription schedule will create [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when transitioning to this phase. The default value is `create_prorations`. This setting controls prorations when a phase is started asynchronously and it is persisted as a field on the phase. It's different from the request-level [proration_behavior](https://stripe.com/docs/api/subscription_schedules/update#update_subscription_schedule-proration_behavior) parameter which controls what happens if the update request affects the billing configuration of the current phase.
            """
            start_date: NotRequired["int|Literal['now']|None"]
            """
            The date at which this phase of the subscription schedule starts or `now`. Must be set on the first phase.
            """
            transfer_data: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseTransferData|None"
            ]
            """
            The data with which to automatically create a Transfer for each of the associated subscription's invoices.
            """
            trial: NotRequired["bool|None"]
            """
            If set to true the entire phase is counted as a trial and the customer will not be charged for any fees.
            """
            trial_end: NotRequired["int|Literal['now']|None"]
            """
            Sets the phase to trialing from the start date to this date. Must be before the phase end date, can not be combined with `trial`
            """

        class ModifyParamsPhaseTransferData(TypedDict):
            amount_percent: NotRequired["float|None"]
            """
            A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination.
            """
            destination: str
            """
            ID of an existing, connected Stripe account.
            """

        class ModifyParamsPhaseItem(TypedDict):
            billing_thresholds: NotRequired[
                "Literal['']|SubscriptionSchedule.ModifyParamsPhaseItemBillingThresholds|None"
            ]
            """
            Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to a configuration item. Metadata on a configuration item will update the underlying subscription item's `metadata` when the phase is entered, adding new keys and replacing existing keys. Individual keys in the subscription item's `metadata` can be unset by posting an empty value to them in the configuration item's `metadata`. To unset all keys in the subscription item's `metadata`, update the subscription item directly or unset every key individually from the configuration item's `metadata`.
            """
            plan: NotRequired["str|None"]
            """
            The plan ID to subscribe to. You may specify the same ID in `plan` and `price`.
            """
            price: NotRequired["str|None"]
            """
            The ID of the price object.
            """
            price_data: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseItemPriceData|None"
            ]
            """
            Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
            """
            quantity: NotRequired["int|None"]
            """
            Quantity for the given price. Can be set only if the price's `usage_type` is `licensed` and not `metered`.
            """
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            """
            A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will override the [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates.
            """

        class ModifyParamsPhaseItemPriceData(TypedDict):
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            product: str
            """
            The ID of the product that this price will belong to.
            """
            recurring: "SubscriptionSchedule.ModifyParamsPhaseItemPriceDataRecurring"
            """
            The recurring components of a price such as `interval` and `interval_count`.
            """
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            """
            Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
            """
            unit_amount: NotRequired["int|None"]
            """
            A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
            """
            unit_amount_decimal: NotRequired["str|None"]
            """
            Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
            """

        class ModifyParamsPhaseItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            """
            Specifies billing frequency. Either `day`, `week`, `month` or `year`.
            """
            interval_count: NotRequired["int|None"]
            """
            The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks).
            """

        class ModifyParamsPhaseItemBillingThresholds(TypedDict):
            usage_gte: int
            """
            Number of units that meets the billing threshold to advance the subscription to a new billing period (e.g., it takes 10 $5 units to meet a $50 [monetary threshold](https://stripe.com/docs/api/subscriptions/update#update_subscription-billing_thresholds-amount_gte))
            """

        class ModifyParamsPhaseInvoiceSettings(TypedDict):
            days_until_due: NotRequired["int|None"]
            """
            Number of days within which a customer must pay invoices generated by this subscription schedule. This value will be `null` for subscription schedules where `billing=charge_automatically`.
            """

        class ModifyParamsPhaseBillingThresholds(TypedDict):
            amount_gte: NotRequired["int|None"]
            """
            Monetary threshold that triggers the subscription to advance to a new billing period
            """
            reset_billing_cycle_anchor: NotRequired["bool|None"]
            """
            Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged.
            """

        class ModifyParamsPhaseAutomaticTax(TypedDict):
            enabled: bool
            """
            Enabled automatic tax calculation which will automatically compute tax rates on all invoices generated by the subscription.
            """

        class ModifyParamsPhaseAddInvoiceItem(TypedDict):
            price: NotRequired["str|None"]
            """
            The ID of the price object.
            """
            price_data: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseAddInvoiceItemPriceData|None"
            ]
            """
            Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
            """
            quantity: NotRequired["int|None"]
            """
            Quantity for this item. Defaults to 1.
            """
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            """
            The tax rates which apply to the item. When set, the `default_tax_rates` do not apply to this item.
            """

        class ModifyParamsPhaseAddInvoiceItemPriceData(TypedDict):
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            product: str
            """
            The ID of the product that this price will belong to.
            """
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            """
            Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
            """
            unit_amount: NotRequired["int|None"]
            """
            A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
            """
            unit_amount_decimal: NotRequired["str|None"]
            """
            Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
            """

        class ModifyParamsDefaultSettings(TypedDict):
            application_fee_percent: NotRequired["float|None"]
            """
            A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
            """
            automatic_tax: NotRequired[
                "SubscriptionSchedule.ModifyParamsDefaultSettingsAutomaticTax|None"
            ]
            """
            Default settings for automatic tax computation.
            """
            billing_cycle_anchor: NotRequired[
                "Literal['automatic', 'phase_start']|None"
            ]
            """
            Can be set to `phase_start` to set the anchor to the start of the phase or `automatic` to automatically change it if needed. Cannot be set to `phase_start` if this phase specifies a trial. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
            """
            billing_thresholds: NotRequired[
                "Literal['']|SubscriptionSchedule.ModifyParamsDefaultSettingsBillingThresholds|None"
            ]
            """
            Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds.
            """
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            """
            Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically` on creation.
            """
            default_payment_method: NotRequired["str|None"]
            """
            ID of the default payment method for the subscription schedule. It must belong to the customer associated with the subscription schedule. If not set, invoices will use the default payment method in the customer's invoice settings.
            """
            description: NotRequired["Literal['']|str|None"]
            """
            Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription.
            """
            invoice_settings: NotRequired[
                "SubscriptionSchedule.ModifyParamsDefaultSettingsInvoiceSettings|None"
            ]
            """
            All invoices will be billed using the specified settings.
            """
            on_behalf_of: NotRequired["Literal['']|str|None"]
            """
            The account on behalf of which to charge, for each of the associated subscription's invoices.
            """
            transfer_data: NotRequired[
                "Literal['']|SubscriptionSchedule.ModifyParamsDefaultSettingsTransferData|None"
            ]
            """
            The data with which to automatically create a Transfer for each of the associated subscription's invoices.
            """

        class ModifyParamsDefaultSettingsTransferData(TypedDict):
            amount_percent: NotRequired["float|None"]
            """
            A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination.
            """
            destination: str
            """
            ID of an existing, connected Stripe account.
            """

        class ModifyParamsDefaultSettingsInvoiceSettings(TypedDict):
            days_until_due: NotRequired["int|None"]
            """
            Number of days within which a customer must pay invoices generated by this subscription schedule. This value will be `null` for subscription schedules where `collection_method=charge_automatically`.
            """

        class ModifyParamsDefaultSettingsBillingThresholds(TypedDict):
            amount_gte: NotRequired["int|None"]
            """
            Monetary threshold that triggers the subscription to advance to a new billing period
            """
            reset_billing_cycle_anchor: NotRequired["bool|None"]
            """
            Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged.
            """

        class ModifyParamsDefaultSettingsAutomaticTax(TypedDict):
            enabled: bool
            """
            Enabled automatic tax calculation which will automatically compute tax rates on all invoices generated by the subscription.
            """

        class ReleaseParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            preserve_cancel_date: NotRequired["bool|None"]
            """
            Keep any cancellation on the subscription that the schedule has set
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    application: Optional[ExpandableField["Application"]]
    """
    ID of the Connect Application that created the schedule.
    """
    canceled_at: Optional[int]
    """
    Time at which the subscription schedule was canceled. Measured in seconds since the Unix epoch.
    """
    completed_at: Optional[int]
    """
    Time at which the subscription schedule was completed. Measured in seconds since the Unix epoch.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    current_phase: Optional[StripeObject]
    """
    Object representing the start and end dates for the current phase of the subscription schedule, if it is `active`.
    """
    customer: ExpandableField["Customer"]
    """
    ID of the customer who owns the subscription schedule.
    """
    default_settings: StripeObject
    end_behavior: Literal["cancel", "none", "release", "renew"]
    """
    Behavior of the subscription schedule and underlying subscription when it ends. Possible values are `release` or `cancel` with the default being `release`. `release` will end the subscription schedule and keep the underlying subscription running.`cancel` will end the subscription schedule and cancel the underlying subscription.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["subscription_schedule"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    phases: List[StripeObject]
    """
    Configuration for the subscription schedule's phases.
    """
    released_at: Optional[int]
    """
    Time at which the subscription schedule was released. Measured in seconds since the Unix epoch.
    """
    released_subscription: Optional[str]
    """
    ID of the subscription once managed by the subscription schedule (if it is released).
    """
    status: Literal[
        "active", "canceled", "completed", "not_started", "released"
    ]
    """
    The present status of the subscription schedule. Possible values are `not_started`, `active`, `completed`, `released`, and `canceled`. You can read more about the different states in our [behavior guide](https://stripe.com/docs/billing/subscriptions/subscription-schedules).
    """
    subscription: Optional[ExpandableField["Subscription"]]
    """
    ID of the subscription managed by the subscription schedule.
    """
    test_clock: Optional[ExpandableField["TestClock"]]
    """
    ID of the test clock this subscription schedule belongs to.
    """

    @classmethod
    def _cls_cancel(
        cls,
        schedule: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.CancelParams"]
    ) -> "SubscriptionSchedule":
        return cast(
            "SubscriptionSchedule",
            cls._static_request(
                "post",
                "/v1/subscription_schedules/{schedule}/cancel".format(
                    schedule=util.sanitize_id(schedule)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def cancel(
        cls,
        schedule: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.CancelParams"]
    ) -> "SubscriptionSchedule":
        ...

    @overload
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.CancelParams"]
    ) -> "SubscriptionSchedule":
        ...

    @class_method_variant("_cls_cancel")
    def cancel(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.CancelParams"]
    ) -> "SubscriptionSchedule":
        return cast(
            "SubscriptionSchedule",
            self._request(
                "post",
                "/v1/subscription_schedules/{schedule}/cancel".format(
                    schedule=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.CreateParams"]
    ) -> "SubscriptionSchedule":
        return cast(
            "SubscriptionSchedule",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.ListParams"]
    ) -> ListObject["SubscriptionSchedule"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["SubscriptionSchedule.ModifyParams"]
    ) -> "SubscriptionSchedule":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "SubscriptionSchedule",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def _cls_release(
        cls,
        schedule: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.ReleaseParams"]
    ) -> "SubscriptionSchedule":
        return cast(
            "SubscriptionSchedule",
            cls._static_request(
                "post",
                "/v1/subscription_schedules/{schedule}/release".format(
                    schedule=util.sanitize_id(schedule)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def release(
        cls,
        schedule: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.ReleaseParams"]
    ) -> "SubscriptionSchedule":
        ...

    @overload
    def release(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.ReleaseParams"]
    ) -> "SubscriptionSchedule":
        ...

    @class_method_variant("_cls_release")
    def release(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.ReleaseParams"]
    ) -> "SubscriptionSchedule":
        return cast(
            "SubscriptionSchedule",
            self._request(
                "post",
                "/v1/subscription_schedules/{schedule}/release".format(
                    schedule=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["SubscriptionSchedule.RetrieveParams"]
    ) -> "SubscriptionSchedule":
        instance = cls(id, **params)
        instance.refresh()
        return instance
